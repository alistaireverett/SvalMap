"""
SvalMap
=========

Python package for simple plotting of data around Svalbard.

Currently limited functionality. Use the sval_plot() function to return an axis
which contains land, ice and water polygons for Svalbard.

Example
---------

import svalmap

ax = svalmap.sval_plot(land=True, ice=True, water=False, ax=None)

"""

from .svalmap import *
