#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Andres Avalos'
SITENAME = 'the Data'
SITEURL = ''
SITETITLE = 'andres avalos'
SITESUBTITLE = 'Data Scientist'
PATH = 'content'
BROWSER_COLOR = '#244444'


TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



# Blogroll
LINKS = None
#(('Pelican', 'http://getpelican.com/'),
         #('Python.org', 'http://python.org/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
         #('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/andresavalos93'),
          ('github', 'https://github.com/afavalos93'),)

THEME = "/home/andresistor/pelican-themes/Flex/"

DEFAULT_PAGINATION = 2


GOOGLE_ANALYTICS = 'UA-83699112-1'
GOOGLE_TAG_MANAGER = 'GTM-NKZR65'



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup','pelican_javascript']

