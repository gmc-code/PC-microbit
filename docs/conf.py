# Configuration file for the Sphinx documentation builder.
# see https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import sphinx_rtd_theme

# Ensure custom extension path is available
sys.path.append(os.path.abspath("./_ext"))

# -- Project information -----------------------------------------------------

project = 'PC-Microbit'
copyright = '2021-26, GMC'
author = 'GMC'

# -- General configuration ---------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx_copybutton',
    'sphinx.ext.todo',
    'sphinx.ext.autodoc',
    'sphinx_togglebutton',
    'sphinx_design',
    "sphinx_new_tab_link",
    "classifying.classifying",  # custom directive
    "ordering.ordering",  # custom directive
    "gapfill.gapfill",  # custom directive
    "cloze.cloze",  # custom directive
    "multichoice.multichoice",  # custom directive
    "labels.labels",  # custom directive
    "sphinx_simplepdf",
]


# for copybutton to allow use of :class: no-copybutton  in code blocks
# copybutton_selector = "div:not(.no-copybutton) > div.highlight > pre"

# for sphinx_new_tab_link  False si default
# new_tab_link_show_external_link_icon = False


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# if using To Dos and want them to showup
todo_include_todos = True

# default python Pygments (syntax highlighting) style to use.
# for other styles see https://pygments.org/docs/lexers/#lexers-for-python-and-related-languages
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------

# The theme to use for HTML and HTML Help pages.
# See the documentation for a list of builtin themes.

html_theme = 'sphinx_rtd_theme'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None
html_title = "PC-Microbit"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# html_static_path = ['../_static/'] # for jupyter

# Use custom css  html_css_files = ["custom.css"]
html_css_files = [
    "css/custom.css",
]

# Custom JS
html_js_files = []

# for rtd



# -- sphinx-rtd-theme Theme Options ------
# See: https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html

html_theme_options = {
    'logo_only': False,  # False so text is shown
    'prev_next_buttons_location': 'both',  # Can be bottom, top, both , or None
    'style_external_links': True,  # True to Add an icon next to external links
    # 'style_nav_header_background': 'blue',
    'style_nav_header_background': 'linear-gradient(to right, blueviolet 15%, limegreen 50%, royalblue 80%)',
    # Toc options;
    'collapse_navigation': True,  # False so nav entries have the [+] icons
    'sticky_navigation': False,  # True so the nav scrolls with main page
    'navigation_depth': 2,  # -1 for no limit, slow to build
    'includehidden': False,  # displays toctree that are hidden
    'titles_only': False  # False so page subheadings are in the nav.
}

# -- RTDs logos -------------------------------
html_favicon = "_static/favicon.ico"
html_logo = "_static/logo_navyblue.png"


# -- simplepdf ------------------------------

simplepdf_vars = {
    # Adjust primary color accent
    "primary": "#89bffa",
    'cover-bg': 'linear-gradient(to right, blueviolet 15%, limegreen 50%, royalblue 80%)',
    # Reduce header/footer spacing to leave more page room
    "top-center-content": '""',
    "top-right-content": '""',
    "bottom-center-content": '"Page " counter(page)',
}