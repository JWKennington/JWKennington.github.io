#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'J. W. Kennington'
SITENAME = 'J. W. Kennington'
COPYRIGHT = AUTHOR
SITEURL = 'https://jwkennington.com/'

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# FEED_ALL_ATOM = None
# AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
FA_SOCIAL = (
    ('beaker', 'https://www.researchgate.net/profile/James_Kennington'),
)

SOCIAL = (
    ('github', 'http://github.com/JWKennington'),
    ('linkedin', 'https://www.linkedin.com/in/jameskennington/'),
    ('twitter', 'https://twitter.com/JwKennington'),
    ('facebook', 'https://www.facebook.com/jimmy.kennington'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme control
THEME = '/Users/jim/repos/professional/jwk-theme'

# Static home page
INDEX_SAVE_AS = 'blog.html'
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARTICLE_ORDER_BY = 'reversed-date'


# CONTOL menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Blog','/blog'),
    ('CV','/pages/cv'),
    ('Code','/pages/code'),
    ('Publications','/pages/publications'),
    # ('Research','/pages/research'),
)

BLOG_PAGE_IMAGE_HEADER = '../images/nyc.png'
ARTICLE_PAGE_IMAGE_HEADER = '../' + BLOG_PAGE_IMAGE_HEADER
SIDEBAR_DISPLAY = ['categories', 'tags']

PLUGIN_PATHS=['/Users/jim/repos/professional/pelican-plugins']
PLUGINS = ['render_math']

LOAD_CONTENT_CACHE = False

MATH_JAX = {'color':'blue'}

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
