#!/usr/bin/python2
# -*- coding: utf-8 -*-
from twython import Twython

APP_KEY = 'QkXeFkMDm6Mx75PzcDQkqg'
APP_SECRET = 'LY0tb8UM0Ye1X0Bk3Z99BsWKXd0I5zoG3A6wfiYErY'
OAUTH_TOKEN = 'Pwjotx1YyaqiVce77HFeOxWJxWvk8KgXYCLykZDL9ik'
OAUTH_TOKEN_SECRET='1893564546-biXRsHcfyqnsTu0Qnaz9rU4BxqeBT4PmFFhWBRH'

twitter  = Twython(APP_KEY, APP_SECRET,
                   OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
search = twitter.cursor(twitter.search, q='Energiewende')
for result in search:
    print result
