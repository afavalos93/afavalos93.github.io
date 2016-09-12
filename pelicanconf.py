#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Andres Avalos'
SITENAME = "Andres' Data Blog"
SITEURL = ''
SITETITLE = 'andres avalos'
SITESUBTITLE = 'Data Scientist'
SITEDESCRIPTION = 'Andres Data Blog'
THEME = "/home/andresistor/pelican-themes/Flex"
PATH = 'content'

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

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/andresavalos93'),
          ('github', 'https://github.com/afavalos93'))

COPYRIGHT_YEAR = 2016

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']