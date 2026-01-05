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
nb_execution_mode = "off"
nb_execution_timeout = -1

# (Optional compatibility: keep these too; harmless if unused)
mystnb_execution_mode = "off"
mystnb_execution_timeout = -1

source_suffix = [".md", ".rst", ".ipynb"]

html_theme = "sphinx_book_theme"
external_toc_path = "_toc.yml"
