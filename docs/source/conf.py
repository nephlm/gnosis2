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

html_css_files = [
    'css/custom.css',
]


html_title = "Gnosis"

# html_theme_options = {
#     "light_logo": "light_logo.png",
#     "dark_logo": "dark_logo.png",
# }

myst_heading_anchors = 3
myst_enable_extensions = [
    "attrs_block",
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

def abbr_fx(term, definition):
    return f'{{abbr}}`{term} ({definition})`'


definitions = {
    'advantage': "Each tier of advantage adds a die of the same size " +
            "as the attribute and only the highest one for each attribute is kept.",
    'adventuring': "This is the part of the shared fictional world where the " +
            "adventure takes place.  The campaign world may be a whole world but if " +
            "the Heroes never leave one city, than the adventuring space is only that city.",
    'Boon': "Boon Definition",
    'Consequence': "Consequence Definition",
    'Creation': "The game world.",
    'Demiurge': ("A less perfect being responsible for the creation of the "
                "material universe, subordinate to the perfect, "
                "purely spiritual creator."),
    'Facts': "Campaign Fact, a fact that is true in the game setting.",
    'Favor': "Favor Definition",
    'Gear': "A type of Boon that represents a piece or set of equipment tied to the Hero.",
    'Locations': "A type of Boon that represents a place or type of place associated with the Hero..",
    'Logos': "Logos Definition",
    'Kith': "A type of Boon that represents one of the Hero's relationships.",
    'Price': "Price Definition",
    'Props': "Props Definition",
    'Strategy': "The set of Boons the player chooses to use for an attribute roll.",
    'Talent': "A type of Boon that is intrinsic to the Hero, such as a learned skill.",
    'Trouble': 'Trouble Definition',
    'xp': 'Experience Points.'
}

# A definition has a synonym such as a plural.
synonyms = {
    'Boons': definitions['Boon'],
    'Consequences': definitions['Consequence'],
    'Strategies': definitions['Strategy'],
    'Talents': definitions['Talent'],
}
definitions.update(synonyms)

abbr_substitutions = {key: abbr_fx(key, val) for key,val in definitions.items()}

abbr_substitutions.update({
    # Non definition substitution are added here.
})

myst_substitutions = abbr_substitutions
