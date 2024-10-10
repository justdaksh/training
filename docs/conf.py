# Configuration file for the Sphinx documentation builder.
# Mastering Plone documentation build configuration file


# -- Path setup --------------------------------------------------------------

from datetime import datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath("."))


# -- Project information -----------------------------------------------------

project = "Plone Training"
copyright = """The text and illustrations in this website are licensed
 by the Plone Foundation under a Creative Commons Attribution 4.0
 International license"""
author = "Plone Community"
trademark_name = "Plone"

now = datetime.now()
year = str(now.year)
# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = year
# The full version, including alpha/beta/rc tags.
release = year

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ""
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = "%B %d, %Y"


# -- General configuration ----------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Add any Sphinx extension module names here, as strings.
# They can be extensions coming with Sphinx (named "sphinx.ext.*")
# or your custom ones.
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_sitemap",
    "sphinxext.opengraph",
]

# For more information see:
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = [
    "deflist",  # You will be able to utilise definition lists
    # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#definition-lists
    "linkify",  # Identify “bare” web URLs and add hyperlinks.
    "colon_fence",  # You can also use ::: delimiters to denote code fences,\
    #  instead of ```.
]

# If true, the Docutils Smart Quotes transform, originally based on SmartyPants
# (limited to English) and currently applying to many languages, will be used
# to convert quotes and dashes to typographically correct entities.
# Note to maintainers: setting this to `True` will cause contractions and
# hyphenated words to be marked as misspelled by spellchecker.
smartquotes = False

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = "sphinx.pygments_styles.PyramidStyle"
pygments_style = "sphinx"

# Options for the linkcheck builder
# Ignore localhost
linkcheck_ignore = [
    r"https?://.*localhost.*",
    r"http://0.0.0.0",
    r"http://127.0.0.1",
    r"http://example.com",
    r"https://github.com/plone/training/issues/new/choose",  # requires auth
    r"https://docs.github.com/en/get-started/.*",  # GitHub docs require auth
    r"https://github.com/plone/mockup/blob/master/mockup/.jshintrc",  # TODO: remove when javascript/development-process.md is updated. See https://github.com/plone/training/issues/611
    r"https://www.dipf.de/.*",  # a timeout from time to time
    r"https://www.linode.com/.*",  # test say 500 Server Error but manually they work
    r"https://www.packtpub.com/.*",  # test say 500 Server Error but manually they work
    # ### Start of list of anchored links
    # Prior to each PloneConf, uncomment these lines to verify that the links work,
    # although the anchor cannot be found.
    # GitHub rewrites anchors with JavaScript.
    # See https://github.com/plone/training/issues/598#issuecomment-1105168109
    # Ignore github.com pages with anchors
    r"https://github.com/.*#.*",
    r"https://plone.github.io/mockup/dev/.*#.*",
    # Ignore other specific anchors
    "https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html#Keywords",
    # ### End of list of anchored links
]
linkcheck_allowed_redirects = {
    # All HTTP redirections from the source URI to the canonical URI will be treated as "working".
    r"https://chrome\.google\.com/webstore/detail/.*": r"https://consent\.google\.com/.*",
}
linkcheck_anchors = True
linkcheck_timeout = 5
linkcheck_retries = 1
linkcheck_rate_limit_timeout = 10

# The suffix of source filenames.
source_suffix = {
    ".md": "markdown",
}

# The master toctree document.
master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_logo = "_static/logo.svg"
html_favicon = "_static/favicon.ico"

html_css_files = ["custom.css", ("print.css", {"media": "print"})]
html_js_files = [
    "patch_scrollToActive.js",
]

html_extra_path = [
    "robots.txt",
]

# Used by sphinx_sitemap to generate a sitemap
html_baseurl = "https://training.plone.org/"
# https://sphinx-sitemap.readthedocs.io/en/latest/advanced-configuration.html#customizing-the-url-scheme
sitemap_url_scheme = "{link}"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_theme_options = {
    "logo": {
        "text": "Plone Training 2024",
    },
    "path_to_docs": "docs",
    "repository_branch": "main",
    "repository_url": "https://github.com/plone/training",
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "article_header_start": ["toggle-primary-sidebar", "chapter-title"],
}


# -- Intersphinx configuration ----------------------------------

# This extension can generate automatic links to the documentation of objects
# in other projects. Usage is simple: whenever Sphinx encounters a
# cross-reference that has no matching target in the current documentation set,
# it looks for targets in the documentation sets configured in
# intersphinx_mapping. A reference like :py:class:`zipfile.ZipFile` can then
# linkto the Python documentation for the ZipFile class, without you having to
# specify where it is located exactly.
#
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
#
intersphinx_mapping = {
    "plone5docs": ("https://5.docs.plone.org/", None),
    "plone6docs": ("https://6.docs.plone.org/", None),
    "python": ("https://docs.python.org/3/", None),
    "training2023": ("https://2023.training.plone.org/", None),
    "training2022": ("https://2022.training.plone.org/", None),
}


# -- GraphViz configuration ----------------------------------

graphviz_output_format = "svg"


# -- OpenGraph configuration ----------------------------------

ogp_site_url = "https://training.plone.org/"
ogp_description_length = 200
ogp_image = "https://training.plone.org/_static/Plone_logo_square.png"
ogp_site_name = "Plone Training"
ogp_type = "website"
ogp_custom_meta_tags = [
    '<meta property="og:locale" content="en_US" />',
]


# -- sphinx.ext.todo -----------------------
todo_include_todos = True  # Uncomment to show todos.


# An extension that allows replacements for code blocks that
# are not supported in `rst_epilog` or other substitutions.
# https://stackoverflow.com/a/56328457/2214933
def source_replace(app, docname, source):
    result = source[0]
    for key in app.config.source_replacements:
        result = result.replace(key, app.config.source_replacements[key])
    source[0] = result


# Dict of replacements.
source_replacements = {
    "{PLONE_BACKEND_VERSION}": "6.0.7",
    "{VOLTO_FRONTEND_VERSION}": "17.0.0-alpha.27",
}


def setup(app):
    app.add_config_value("source_replacements", {}, True)
    app.connect("source-read", source_replace)
