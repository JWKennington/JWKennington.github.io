#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import pelican_cite_nice
import pelican_ga_pageview
import pelican_github_activity
import pelican_render_math

import jwk_theme

AUTHOR = 'Jim Kennington'
SITENAME = 'Jim W. Kennington'
COPYRIGHT = AUTHOR
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'
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
    ('amilia', 'http://adsabs.harvard.edu/cgi-bin/nph-abs_connect?cookie=5db7b35acd30413'),
    ('orcid', 'https://orcid.org/0000-0002-6899-3833'),
    ('researchgate', 'https://www.researchgate.net/profile/James_Kennington'),
    ('github', 'https://github.com/JWKennington'),
    ('linkedin', 'https://www.linkedin.com/in/jameskennington/'),
)

SOCIAL = (
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme control
THEME = jwk_theme.THEME_PATH
# THEME = '/Users/jim/repos/professional/jim/jwk-theme/jwk_theme'

# Static home page
INDEX_SAVE_AS = 'blog.html'
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARTICLE_ORDER_BY = 'reversed-date'

# CONTOL menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Blog', '/blog'),
    ('CV', '/pages/cv'),
    # ('Code', '/pages/code'),
    # ('Publications', '/pages/publications'),
    ('Research', '/pages/research'),
    ('Resources', '/pages/resources'),
)

BLOG_PAGE_IMAGE_HEADER = '../images/bookshelf.png'
ARTICLE_PAGE_IMAGE_HEADER = '../' + BLOG_PAGE_IMAGE_HEADER
SIDEBAR_DISPLAY = ['categories', 'tags']

PLUGIN_PATHS = ['/Users/jim/repos/professional/pelican-plugins']

PLUGINS = [
    pelican_cite_nice,
    pelican_render_math,
    pelican_github_activity,
    pelican_ga_pageview,
]

LOAD_CONTENT_CACHE = False

MATH_JAX = {'color': 'blue'}

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

DISQUS_SITENAME = 'jwkennington'
DISQUS_SITEURL = 'jwkennington.com'

# GITHUB
GITHUB_ACTIVITY_FEED = 'https://github.com/JWKennington.atom'
GITHUB_ACTIVITY_MAX_ENTRIES = 5
GITHUB_REPO_IGNORE = [
    'JWKennington.github.io',
    'HRKennington.github.io',
    'jwk-theme',
    'hrk-theme',
    'pelican-ga-pageview',
    'pelican-render-math',
    'pelican-cite-nice',
    'pelican-github-activity',
    'pelican-cite'
]

# GOOGLE ANALYTICS
GOOGLE_ANALYTICS = 'UA-135655259-1'
GOOGLE_SERVICE_ACCOUNT = 'sitetracker@high-unity-233520.iam.gserviceaccount.com'
GOOGLE_KEY_FILE = './client_private.p12'
GA_START_DATE = '2019-01-01'
GA_END_DATE = 'today'
GA_METRIC = 'ga:pageviews'

# CITATIONS
PUBLICATIONS_SRC = 'content/references.bib'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
}
