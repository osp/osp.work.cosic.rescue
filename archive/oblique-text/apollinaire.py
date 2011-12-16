#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from ui_principal import Ui_MainWindow
from oblique_text import make_oblique_4

class MonAppli(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("GTK+"))
        QtGui.QApplication.setPalette(QtGui.QApplication.style().standardPalette())

        self.is_reversed = False
        self.letter_spacing = 1
        self.line_spacing = 1
        self.slant = 1
        self.source = "Il pleut des voix de femmes..."

        # Configure l'interface utilisateur.
        self.setupUi(self)
        self.actionQuit.triggered.connect(QtGui.qApp.quit)

        self.source_widget.setPlainText(self.source)
        self.connect(self.source_widget, QtCore.SIGNAL('textChanged()'), \
                self.source_changed) 

        self.slant_widget.setValue(self.slant)
        self.connect(self.slant_widget, QtCore.SIGNAL('valueChanged(int)'), \
                self.slant_changed) 

        self.letter_spacing_widget.setValue(self.letter_spacing)
        self.connect(self.letter_spacing_widget, QtCore.SIGNAL('valueChanged(int)'), \
                self.letter_spacing_changed) 

        self.line_spacing_widget.setValue(self.line_spacing)
        self.connect(self.line_spacing_widget, QtCore.SIGNAL('valueChanged(int)'), \
                self.line_spacing_changed) 

        #self..setValue(self.line_spacing)
        self.connect(self.is_reversed_widget, QtCore.SIGNAL('stateChanged(int)'), \
                self.is_reversed_changed) 

        self.do_it()

    def source_changed(self):
        sender = self.sender()
        self.source = unicode(sender.toPlainText())
        #print(self.source)
        #print(repr(self.source))
        #print(type(self.source))
        #print(repr(self.source))
        self.do_it()

    def letter_spacing_changed(self):
        sender = self.sender()
        self.letter_spacing = sender.value()
        self.do_it()

    def line_spacing_changed(self):
        sender = self.sender()
        self.line_spacing = sender.value()
        self.do_it()

    def slant_changed(self):
        sender = self.sender()
        self.slant = sender.value()
        self.do_it()

    def is_reversed_changed(self):
        sender = self.sender()
        self.is_reversed = sender.checkState()
        self.do_it()

    def do_it(self):
        self.result_widget.setPlainText(make_oblique_4(self.source, \
                slant=self.slant, line_spacing=self.line_spacing, \
                letter_spacing=self.letter_spacing, \
                reverse=self.is_reversed).decode('utf-8'))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MonAppli()

    window.show()
    sys.exit(app.exec_())
