test_mode = False # use test wikipedia instead of normal one if True
user_name = u'Lonjers' #should be bot name in production
bot_user_name = u'User:ProjectRequestedPagesBot'
# normally posts to something like
# config.bot_user_name + '/Most Requested ' + project_name + ' Pages'
# but you can specify specific pages if this is True
allow_target_pages = True
max_catalog_pages = 30 # set to None to do all
article_namespace_only = False # do not list links to non article wiki pages
actually_edit = True # if false only prints dictionary of redlinks does not post
users_to_notify_on_error = ['Lonjers', 'Wugapodes']
