from config import user_name, test_mode
#use_api_login = True # not sure what this was for

console_encoding = 'utf-8'
if test_mode:
    mylang = 'test'
    family = 'test'
else:
    mylang = 'en'
    family = 'wikipedia'

usernames[family][mylang] = user_name

