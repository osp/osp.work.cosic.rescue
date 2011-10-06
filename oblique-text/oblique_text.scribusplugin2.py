#!/usr/bin/env python


import scribus
from oblique_text import make_oblique_3

scribus.setText(make_oblique_3(scribus.getAllText()))
