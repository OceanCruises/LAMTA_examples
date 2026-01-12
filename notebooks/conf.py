# notebooks/conf.py
project = "LAMTA Examples"
author = "OceanCruises"

master_doc = "index"

extensions = [
    "myst_nb",
    "sphinx_book_theme",
    "sphinx_external_toc",
    "sphinx_design"
]

# myst-nb: do not execute, render stored outputs
nb_execution_mode = "off"
nb_execution_timeout = -1

source_suffix = [".md", ".rst", ".ipynb"]

html_theme = "sphinx_book_theme"
external_toc_path = "_toc.yml"
