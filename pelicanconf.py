"""Pelican settings for aporia.barcelona. Local build; publishconf.py overrides for production."""

AUTHOR = "Aporia Barcelona"
SITENAME = "Aporia Barcelona"
SITEURL = ""
DEFAULT_LANG = "es"
TIMEZONE = "Europe/Madrid"

PATH = "content"
ARTICLE_PATHS = ["eventos"]   # one Markdown file per event, from milestone 2
PAGE_PATHS = ["pages"]
STATIC_PATHS = []

THEME = "theme"

# Only the home page for now. Categories, tags, authors, and archives are off: the site has one kind of content.
DIRECT_TEMPLATES = ["index"]
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""

# No feeds yet
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

RELATIVE_URLS = True
