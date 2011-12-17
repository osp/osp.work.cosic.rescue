# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apollinaire.ui'
#
# Created: Sun Oct  9 13:45:04 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(522, 560)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_slant = QtGui.QLabel(self.centralwidget)
        self.label_slant.setText(QtGui.QApplication.translate("MainWindow", "Slant", None, QtGui.QApplication.UnicodeUTF8))
        self.label_slant.setObjectName(_fromUtf8("label_slant"))
        self.verticalLayout.addWidget(self.label_slant)
        self.slant_widget = QtGui.QSpinBox(self.centralwidget)
        self.slant_widget.setObjectName(_fromUtf8("slant_widget"))
        self.verticalLayout.addWidget(self.slant_widget)
        self.label_letter_spacing = QtGui.QLabel(self.centralwidget)
        self.label_letter_spacing.setText(QtGui.QApplication.translate("MainWindow", "Letter Spacing", None, QtGui.QApplication.UnicodeUTF8))
        self.label_letter_spacing.setObjectName(_fromUtf8("label_letter_spacing"))
        self.verticalLayout.addWidget(self.label_letter_spacing)
        self.letter_spacing_widget = QtGui.QSpinBox(self.centralwidget)
        self.letter_spacing_widget.setObjectName(_fromUtf8("letter_spacing_widget"))
        self.verticalLayout.addWidget(self.letter_spacing_widget)
        self.label_line_spacing = QtGui.QLabel(self.centralwidget)
        self.label_line_spacing.setText(QtGui.QApplication.translate("MainWindow", "Line spacing", None, QtGui.QApplication.UnicodeUTF8))
        self.label_line_spacing.setObjectName(_fromUtf8("label_line_spacing"))
        self.verticalLayout.addWidget(self.label_line_spacing)
        self.line_spacing_widget = QtGui.QSpinBox(self.centralwidget)
        self.line_spacing_widget.setObjectName(_fromUtf8("line_spacing_widget"))
        self.verticalLayout.addWidget(self.line_spacing_widget)
        self.is_reversed_widget = QtGui.QCheckBox(self.centralwidget)
        self.is_reversed_widget.setText(QtGui.QApplication.translate("MainWindow", "Is Reversed?", None, QtGui.QApplication.UnicodeUTF8))
        self.is_reversed_widget.setObjectName(_fromUtf8("is_reversed_widget"))
        self.verticalLayout.addWidget(self.is_reversed_widget)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.splitter)
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_source = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_source.setText(QtGui.QApplication.translate("MainWindow", "Source", None, QtGui.QApplication.UnicodeUTF8))
        self.label_source.setObjectName(_fromUtf8("label_source"))
        self.verticalLayout_5.addWidget(self.label_source)
        self.source_widget = QtGui.QPlainTextEdit(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        self.source_widget.setFont(font)
        self.source_widget.setObjectName(_fromUtf8("source_widget"))
        self.verticalLayout_5.addWidget(self.source_widget)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.splitter)
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_result = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_result.setText(QtGui.QApplication.translate("MainWindow", "Result", None, QtGui.QApplication.UnicodeUTF8))
        self.label_result.setObjectName(_fromUtf8("label_result"))
        self.verticalLayout_4.addWidget(self.label_result)
        self.result_widget = QtGui.QPlainTextEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        self.result_widget.setFont(font)
        self.result_widget.setObjectName(_fromUtf8("result_widget"))
        self.verticalLayout_4.addWidget(self.result_widget)
        self.horizontalLayout_3.addWidget(self.splitter)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 522, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuG = QtGui.QMenu(self.menubar)
        self.menuG.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuG.setObjectName(_fromUtf8("menuG"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Exit Application", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuG.addAction(self.actionQuit)
        self.menubar.addAction(self.menuG.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.slant_widget, self.letter_spacing_widget)
        MainWindow.setTabOrder(self.letter_spacing_widget, self.line_spacing_widget)
        MainWindow.setTabOrder(self.line_spacing_widget, self.is_reversed_widget)
        MainWindow.setTabOrder(self.is_reversed_widget, self.source_widget)
        MainWindow.setTabOrder(self.source_widget, self.result_widget)

    def retranslateUi(self, MainWindow):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

