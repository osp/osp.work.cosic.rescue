#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
"""

import sys
from PyQt4 import QtGui, QtCore
from oblique_text import make_oblique_4


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.is_reversed = False
        self.letter_spacing = 1
        self.line_spacing = 1
        self.slant = 1
        self.source = "Hello\nWorld"
        self.initUI()
        
    def initUI(self):

        source = QtGui.QPlainTextEdit()
        self.connect(source, QtCore.SIGNAL('textChanged()'), self.source_changed) 

        self.result = QtGui.QTextEdit()
        #self.result.setFontFamily("Mono")
        self.result.setStyleSheet("font-family: Mono;")

        slant = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.connect(slant, QtCore.SIGNAL('valueChanged(int)'), self.slant_changed) 

        letter_spacing = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.connect(letter_spacing, QtCore.SIGNAL('valueChanged(int)'), self.letter_spacing_changed) 

        line_spacing = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.connect(line_spacing, QtCore.SIGNAL('valueChanged(int)'), self.line_spacing_changed) 

        qbtn = QtGui.QPushButton('Quit')
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(qbtn)

        grid = QtGui.QGridLayout()
        grid.addWidget(QtGui.QLabel('Source'), 0, 0)
        grid.addWidget(source, 1, 0)
        grid.addWidget(QtGui.QLabel('Letter Spacing'), 2, 0)
        grid.addWidget(letter_spacing, 3, 0)
        grid.addWidget(QtGui.QLabel('Line Spacing'), 4, 0)
        grid.addWidget(line_spacing, 5, 0)
        grid.addWidget(QtGui.QLabel('Slant'), 6, 0)
        grid.addWidget(slant, 7, 0)
        grid.addWidget(QtGui.QLabel('Result'), 8, 0)
        grid.addWidget(self.result, 9, 0)
        grid.addWidget(qbtn, 10, 0)

        self.setLayout(grid)   
        
        self.move(300, 150)
        self.setWindowTitle('Calculator')    
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def source_changed(self):
        """docstring for slider_changed"""
        sender = self.sender()
        self.source = sender.toPlainText()
        self.do_it()

    def letter_spacing_changed(self):
        """docstring for slider_changed"""
        sender = self.sender()
        self.letter_spacing = sender.value()
        self.do_it()

    def line_spacing_changed(self):
        """docstring for slider_changed"""
        sender = self.sender()
        self.line_spacing = sender.value()
        self.do_it()

    def slant_changed(self):
        """docstring for slider_changed"""
        sender = self.sender()
        self.slant = sender.value()
        self.do_it()

    def do_it(self):
        self.result.setPlainText(make_oblique_4(self.source, slant=self.slant, line_spacing=self.line_spacing, letter_spacing=self.letter_spacing).decode('utf-8'))
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    
