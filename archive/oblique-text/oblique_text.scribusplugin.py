#!/usr/bin/env python


import scribus
from oblique_text import make_oblique

scribus.setText(make_oblique(scribus.getAllText()))
