#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = 'Heuze Florent'
SITEURL = 'https://heuzef.com'
SITESUBTITLE = """
Les notes excentriques d'un bidouilleur.
"""
DEFAULT_PAGINATION = 5
TYPOGRIFY = True

LINKS = (
    ('<i class="fa fa-file-pdf"></i> CV', 'https://cv.heuzef.com'),
    ('<i class="fa fa-envelope"></i> contact', 'contact.html'),
)

FOOTER_LINKS = (
    ('<i class="fa fa-home"></i> Accueil', 'index.html'),
    ('<i class="fa fa-cubes"></i> Catégories', 'categories.html'),
    ('<i class="fa fa-tags"></i> Tags', 'tags.html'),
)

AUTHOR = 'Heuzef'
SITEIMAGE = "assets/logo_heuzef_hd.png"

# Links
ICONS = (
            ('linkedin', 'https://www.linkedin.com/in/heuzef/'),
            ('git', 'https://github.com/heuzef'),
            ('fas fa-heartbeat', 'https://status.heuzef.com'),
            ('fas fa-map', 'https://network.heuzef.com'),
            ('rss', 'https://heuzef.com/feeds/all.atom.xml'),
         )

PATH = 'content'
ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'notes/{slug}/'
ARTICLE_SAVE_AS = 'notes/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
STATIC_PATHS = ['assets', 'files']
EXTRA_PATH_METADATA = {
        'assets/android-chrome-72x72.png': {'path': 'android-chrome-72x72.png'},
        'assets/browserconfig.xml': {'path': 'browserconfig.xml'},
        'assets/favicon-32x32.png': {'path': 'favicon-32x32.png'},
        'assets/mstile-150x150.png': {'path': 'mstile-150x150.png'},
        'assets/site.webmanifest': {'path': 'site.webmanifest'},
        'assets/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
        'assets/favicon-16x16.png': {'path': 'favicon-16x16.png'},
        'assets/favicon.ico': {'path': 'favicon.ico'},
        'assets/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'},
}

PAGE_URL = 'page/{slug}/'
# PAGE_SAVE_AS = 'page/{slug}/index.html'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
TAG_FEED_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'themes/pelican-alchemy/alchemy'
PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bootstrapify']

BOOTSTRAPIFY = {
        'table': ['table', 'table-striped', 'table-hover'],
        'img': ['img-fluid'],
        'blockquote': ['blockquote'],
}

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'
# BOOTSTRAP_CSS: URL of Bootstrap CSS file. Use this to enable Boostwatch themes.
# FONTAWESOME_CSS: URL of Font Awesome CSS file. Use this if you wish to use CDN provided version instead of the bundled one.
PYGMENTS_STYLE = 'manni'
HIDE_AUTHORS = True
RFG_FAVICONS = True 
# THEME_CSS_OVERRIDES: Sequence of stylesheet URLs to override CSS provided by theme. Both relative and absolute URLs are supported.
# THEME_JS_OVERRIDES: Sequence of JavaScript URLs to enable with this theme. Alchemy uses no JS by default. Both relative and absolute URLs are supported.
