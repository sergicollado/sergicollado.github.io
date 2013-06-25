#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sergi Collado'
SITENAME = u'Sergi Collado'
SITEURL = 'http://sergicollado.com'
GITHUB_URL = 'http://github.com/sergicollado/'
THEME = "pelican-chunk-master"
DISQUS_SITENAME = "sergicollado"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
          ('Becode', 'https://becodemyfriend.com'),
          ('GIT-HUB', 'https://github.com/sergicollado'),
        )

# Social widget
SOCIAL = (('Linkedin', 'http://www.linkedin.com/in/sergicollado'),
          ('google+', 'https://plus.google.com/u/0/108686854890472733391/about'),)

DEFAULT_PAGINATION = 10


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True 


#DEFAULT_DATE_FORMAT = ('%b %d %Y') : suggested date format
SITESUBTITLE = ''
#FOOTER_TEXT = 'Replace pelican credit'
DISPLAY_CATEGORIES_ON_MENU = False
#LINKS = (('Site', 'http://url.com'), ('Site 2', 'http://another.url.com'))
SINGLE_AUTHOR = True
MINT = True
GOOGLE_ANALYTICS = """<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-41990150-1', 'sergicollado.com');
  ga('send', 'pageview');
</script>"""
