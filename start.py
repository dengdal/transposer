#!/usr/bin/python

import sys
from PyQt4 import QtCore, QtGui
from transposerGui import Ui_Transposer
import transposerLib

inpFromKey = ''
inpToKey = ''

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Transposer()
        self.ui.setupUi(self)
        # here we connect signals with our slots
        self.ui.fromKeylistWidget.currentItemChanged.connect(self.setFromKey)
        self.ui.toKeylistWidget.currentItemChanged.connect(self.setToKey)
        self.ui.transpose.clicked.connect(self.transpose)
    def setFromKey(self, curr, prev):
        global inpFromKey 
        inpFromKey = str(curr.text())
    def setToKey(self, curr, prev):
        global inpToKey
        inpToKey = str(curr.text())
    def transpose(self):
        global inpFromKey
        global inpToKey
        steps = transposerLib.calcNoOfSteps(inpFromKey, inpToKey)
        fromSong = self.ui.textEdit.toPlainText()
        toSong = transposerLib.transpose(steps, fromSong)
        self.ui.textEdit.setText(str(toSong))
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
