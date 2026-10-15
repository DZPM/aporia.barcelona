"""Pelican settings for aporia.barcelona. Local build; publishconf.py overrides for production."""

AUTHOR = "Aporia Barcelona"
SITENAME = "Aporia Barcelona"
SITEURL = ""
DEFAULT_LANG = "es"
TIMEZONE = "Europe/Madrid"

PATH = "content"
ARTICLE_PATHS = ["eventos"]   # one Markdown file per event, from milestone 2
PAGE_PATHS = ["pages"]

THEME = "theme"

# An Event is an article: content/eventos/NN-slug.md, served at /eventos/NN-slug/ (docs/adr/0002).
# Its Date is the day of the meetup, not the day the page was written.
# An Event is an article: content/eventos/NN-slug.md, served at /eventos/NN-slug/ (docs/adr/0002).
# Its Date is the day of the meetup, not the day the page was written.
ARTICLE_URL = "eventos/{slug}/"
ARTICLE_SAVE_AS = "eventos/{slug}/index.html"
DRAFT_SAVE_AS = ""   # no drafts: an Event enters the repository when it is ready to publish
DRAFT_URL = ""
PATH_METADATA = r"(?P<category>eventos)/.*"   # no category pages, but Pelican 4.12 reads article.category

# Pages and Persons are read, not written: a page names its own address with Save_as (index.md is the home page,
# 404.md the not found page), and a Person (content/personas/, docs/adr/0003) is shown inside the home page only.
PAGE_PATHS = ["pages", "personas"]
PAGE_URL = ""
PAGE_SAVE_AS = ""
STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {   # the icons at the root, where browsers look for them; the AB mark is provisional, until there is a logo
    "extra/favicon.svg": {"path": "favicon.svg"},
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
}

# The only direct template is the sitemap: the home page is content/pages/index.md. Categories, tags, authors, and
# archives are off.
DIRECT_TEMPLATES = ["sitemap"]
SITEMAP_SAVE_AS = "sitemap.xml"
DEFAULT_PAGINATION = False
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

# Dates in Spanish, without a locale: the CI runner has only the C locale
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

MENU = [("Encuentros", "/#encuentros"), ("Sobre nosotros", "/#nosotros")]

# The links a Person can have, shown as icons under the name, in this order: frontmatter key, label, and icon in
# theme/templates/icons/ (the brand icons are the ones davidarcos.net uses). A link with no icon shows its label.
# Web is not here: it is the link of the name.
PERSONA_LINKS = [("linkedin", "LinkedIn", "linkedin"), ("x", "X", "x"), ("bluesky", "Bluesky", None), ("github", "GitHub", "github")]
