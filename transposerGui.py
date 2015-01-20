# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transposerGui.ui'
#
# Created: Tue Jan 20 13:43:39 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Transposer(object):
    def setupUi(self, Transposer):
        Transposer.setObjectName(_fromUtf8("Transposer"))
        Transposer.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Transposer)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.transpose = QtGui.QPushButton(self.centralwidget)
        self.transpose.setGeometry(QtCore.QRect(170, 490, 98, 27))
        self.transpose.setObjectName(_fromUtf8("transpose"))
        self.exit = QtGui.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(290, 490, 98, 27))
        self.exit.setObjectName(_fromUtf8("exit"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(340, 180, 104, 78))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        Transposer.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Transposer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Transposer.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Transposer)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Transposer.setStatusBar(self.statusbar)

        self.retranslateUi(Transposer)
        QtCore.QObject.connect(self.exit, QtCore.SIGNAL(_fromUtf8("clicked()")), Transposer.close)
        QtCore.QMetaObject.connectSlotsByName(Transposer)

    def retranslateUi(self, Transposer):
        Transposer.setWindowTitle(_translate("Transposer", "Transposer", None))
        self.transpose.setText(_translate("Transposer", "Transpose", None))
        self.exit.setText(_translate("Transposer", "Exit", None))

