# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Cloud2Mesh-Docs'
copyright = '2025, Niklas Wockenfuß'
author = 'Niklas Wockenfuß'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',        # Automatische Dokumentation von Python-Modulen
    'sphinx.ext.napoleon',      # Unterstützung für Google- und NumPy-Stil-Dokumentationen
    'myst_parser',               # Unterstützung für Markdown-Dateien
    'sphinx.ext.mathjax',
    'sphinx_copybutton'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = ['.rst', '.md']

# -- autodoc config
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
autodoc_mock_imports = ["numpy"]
autodoc_member_order = 'bysource'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_title = project
html_short_title = project.split('-')[0]
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']