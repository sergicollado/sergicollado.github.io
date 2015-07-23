#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'sergicollado@gmail.com'
SITENAME = 'sergiDev'
SITEURL = 'http://localhost:8000/'
SITESUBTITLE = 'TDD Developer, Python, Agile Javascript coder and better human, I like vegetarian food and GameDev.'
TAGLINE = 'Coder and better human, I like vegetarian food and GameDev.'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin-square', 'http://www.linkedin.com/in/sergicollado'),
          ('google-plus', 'https://plus.google.com/u/0/108686854890472733391/about'),
          ('twitter-square', 'https://twitter.com/circun4'),)


DEFAULT_PAGINATION = 10
THEME = "themes/pure-single"
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


DISQUS_SITENAME = "sergicollado"
DISQUS_ON_PAGES = True
GOOGLE_ANALYTICS = "UA-41990150-1"

COVER_IMG_URL = 'images/side.png'
PROFILE_IMG_URL = 'images/cosmo.png'
