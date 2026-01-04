# notebooks/conf.py
from pathlib import Path
import sys

project = "LAMTA Examples"
author = "OceanCruises"

extensions = [
    "myst_parser",
    "sphinx_book_theme",
    "sphinx_external_toc",
    "sphinx_design",
]

# Tell Sphinx where the book lives
master_doc = "index"
source_suffix = {".md": "markdown", ".rst": "restructuredtext"}

# Jupyter Book configuration
html_theme = "sphinx_book_theme"

# Required by sphinx_external_toc (used by Jupyter Book)
external_toc_path = "_toc.yml"
