# notebooks/conf.py
project = "LAMTA Examples"
author = "OceanCruises"

extensions = [
    "myst_nb",
    "sphinx_book_theme",
    "sphinx_external_toc",
    "sphinx_design",
]

master_doc = "index"

# Do not execute notebooks during docs build (render stored outputs)
mystnb_execute = "off"

source_suffix = [".md", ".rst", ".ipynb"]

html_theme = "sphinx_book_theme"
external_toc_path = "_toc.yml"
