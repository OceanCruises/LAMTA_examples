# notebooks/conf.py
from pathlib import Path
import yaml

project = "LAMTA Examples"
author = "OceanCruises"

master_doc = "index"

extensions = [
    "myst_nb",
    "sphinx_book_theme",
    "sphinx_external_toc",
    "sphinx_design",
    "sphinx_jinja",
]

myst_enable_extensions = ["colon_fence"]

# myst-nb: do not execute, render stored outputs
nb_execution_mode = "off"
nb_execution_timeout = -1

source_suffix = [".md", ".rst", ".ipynb"]

html_theme = "sphinx_book_theme"
external_toc_path = "_toc.yml"

# Jinja gallery support
HERE = Path(__file__).parent
gallery_path = HERE / "gallery.yml"

gallery_data = []
if gallery_path.exists():
    gallery_data = yaml.safe_load(gallery_path.read_text(encoding="utf-8")) or []

# Tell sphinx-jinja which source files are Jinja templates
jinja_templates = ["notebooks_overview.md"]

# Provide variables accessible inside the template
jinja_contexts = {
    "notebooks_overview": {
        "data": gallery_data,
    }
}
