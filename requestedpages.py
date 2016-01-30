#!/usr/bin/python
import pywikibot
import config
from pywikibot import pagegenerators

'''
multiple links on a page only counted once?
should we be more restrictive about what links should count
set up to run automatically
'''

def create_request_list(site, project_name, category_name, threshold, target_page):
    '''
    Scans the category and creates the requested links page
    project_name is purely to decide what page to put the list on
    '''
    cat = pywikibot.Category(site, category_name)
    gen = pagegenerators.CategorizedPageGenerator(cat)
    redlinks = {}
    for i, page in enumerate(gen):
        if config.max_catalog_pages is not None:
            if i > config.max_catalog_pages:
                break

        #article = page.toggleTalkPage()
        linkgen = page.linkedPages()
        for link in linkgen:
            if not link.exists():
            	# if configured to only include articles, and link is to
            	# a namespace other than an article, it does not add it to the list
            	if config.article_namespace_only and link.namespace() != 0:
            		continue
                if link.title() in redlinks:
                    redlinks[link.title()] = redlinks[link.title()] + 1
                else:
                    redlinks[link.title()] = 1
    write_listed_links(site, redlinks, target_page, project_name, threshold)


def write_listed_links(site, redlinks, target_page, project_name, threshold):
    '''
    Given a ditionary of the requested links and frequencies
    Write them as a sorted list to the appropriate page
    '''
    # Writing output to page
    requested_links_page_name = config.bot_user_name + '/Most Requested ' + project_name + ' Pages'
    listpage = pywikibot.Page(site, requested_links_page_name)
    if len(redlinks) < 1:
        text = 'No redlinks found'
        listpage.put(text, summary='No redlinks found', minorEdit=False)
        if target_page != '' and config.allow_target_pages:
            listpage = pywikibot.Page(site, target_page)
            listpage.put(text, summary='No redlinks found', minorEdit=False)
    else:
        text = create_page_text(redlinks, threshold)
        summary = 'Adding the {} most requested articles in the {} scope'
        summary = summary.format(str(len(redlinks)), project_name)
        listpage.put(text, summary=summary, minorEdit=False)
        if target_page != '' and config.allow_target_pages:
            listpage = pywikibot.Page(site, target_page)
            listpage.put(text, summary=summary, minorEdit=False)


def create_page_text(dictionary, thresh):
    '''
    Returns the text for the requested link page
    '''
    text = ''
    entries = sort_dict(dictionary)
    for entry in entries:
        #only includes entry if number of links is greater than the project specified threshold
        if entry[1] > thresh:
            text = text + '# [[' + entry[0] + ']] &mdash; ' + str(entry[1]) + '\n'
    return text

def sort_dict(dictionary):
    '''
    Returns list of articles by number of requests
    '''
    entries = []
    for key in dictionary:
        entries.append([key, dictionary[key]])
    sorted_entries = reversed(sort(entries))
    return sorted_entries


def sort(array):
    '''
     quicksort the entries
     could just use python build  in sort but leaving because this is cooler
    '''
    ls = []
    eq = []
    gr = []
    if len(array) > 1:
        pivot = array[0][1]
        for x in array:
            if x[1] < pivot:
                ls.append(x)
            elif x[1] == pivot:
                eq.append(x)
            elif x[1] > pivot:
                gr.append(x)
        return sort(ls)+eq+sort(gr)
    else:
        return array

def get_projects(site):
    projects = list()
    master = pywikibot.Page(site, config.bot_user_name + '/Master')
    mastertext = master.get()
    for line in mastertext.splitlines():
        if line != '':
            line = line.split(',')
            projects.append(line)
    return projects


def main():
    site = pywikibot.Site()
    projects = get_projects(site)

    for project in projects:
        project_name = project[0] #first item on a line is the name of the wikiproject
        category_name = project[1] #second item on a line is the category name
        given_threshold = project[2]
        target_page = project[3]
        #checks to make sure threshold is an actual integer and that it is not negative
        if given_threshold.isdigit() and int(given_threshold) > 0:
            threshold = int(given_threshold)
        else:
            threshold = 0 #defaults to listing every entry
        create_request_list(site, project_name, category_name, threshold, target_page)


if __name__ == '__main__':
    main()
    # site = pywikibot.Site()
    # print(get_projects(site))
