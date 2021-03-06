#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Bruno Masoller'
SITENAME = 'Portafolio de Machine Learning'
SITETITLE = AUTHOR
SITEURL = 'https://brunomaso1.github.io/ml-porfolio'
#SITEURL = ''
SITESUBTITLE = 'Portafolio de Machine Learning'
SITEDESCRIPTION = 'Portafolio que muestra articulos de ML, desarrollados tanto en Python como RapidMiner'
SITELOGO = 'https://s.gravatar.com/avatar/38da6c883dc55b18f3ac1fb8d25bed67?s=120'
FAVICON = SITEURL + '/img/favicon.ico'
BROWSER_COLOR = '#333333'
#PYGMENTS_STYLE = 'fruity' # Para poner un tema de este estilo, hay que sustituir los area_input que genera el plugin ipynb. Este plugin genera un fondo blanco, hay que sustituirlo por negro con javascript.

ROBOTS = 'index, follow'

THEME = './pelican-themes/Flex'
PATH = 'content'
TIMEZONE = 'America/Argentina/Buenos_Aires'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
MAIN_MENU = True
HOME_HIDE_TAGS = True

INDEX_SAVE_AS = 'blog_index.html'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/brunomaso1'),
          ('github', 'https://github.com/brunomaso1'))

MENUITEMS = (('CRISP-DM', SITEURL + '/pages/crisp-dm.html'),
			('Index', SITEURL + '/blog_index.html'),
			('Categories', SITEURL + '/categories.html'),			 
             ('Tags', SITEURL + '/tags.html'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2016

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['ipynb.markup', 'i18n_subsites', 'assets', 'render_math']
I18N_TEMPLATES_LANG = 'en'

STATIC_PATHS = ['img', 'posts/post-img', 'posts/post-datasets',  'posts/rm-processes', 'extra']

EXTRA_PATH_METADATA = {
   'extra/custom.css': {'path': 'static/custom.css'},
}

CUSTOM_CSS = 'static/custom.css'