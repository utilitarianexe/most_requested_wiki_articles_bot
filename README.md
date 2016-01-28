# most_requested_wiki_articles_bot
The goal is to list the most referenced articles in a wikipedia project that lack a article page.

Your are going to need to install pywikibot and might need something like
export PYTHONPATH="${PYTHONPATH}:/home/peter/project/core/"

Use config.py to configure. Currently set up to use test.wikipedia.org using my personal user name. The normal bot pages(on the test wiki) are still used to decide what projects to use and for output. Change to your user name to test. It will ask you your password on first run. For production use the bots actual name.

Most of the code written by Wugapodes with clean up and bug fixes by Peter Lonjers.

The bot page is at https://en.wikipedia.org/wiki/User:ProjectRequestedPagesBot
