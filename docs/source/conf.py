# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Gnosis 2"
copyright = "2024, Nephlm"
author = "Nephlm"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx_inline_tabs", "sphinx_design"]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]

html_title = "Gnosis"

# html_theme_options = {
#     "light_logo": "light_logo.png",
#     "dark_logo": "dark_logo.png",
# }

myst_heading_anchors = 3
myst_enable_extensions = [
    # "amsmath",
    "colon_fence",
    "deflist",
    # "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]
