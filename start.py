#!/usr/bin/python

import sys
from PyQt4 import QtCore, QtGui
from transposerGui import Ui_Transposer

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Transposer()
        self.ui.setupUi(self)
        # here we connect signals with our slots
        self.ui.transpose.clicked.connect(self.transpose)
        self.ui.fromKeylistWidget.currentItemChanged.connect(self.setFromKey)
        self.ui.toKeylistWidget.clicked.connect(self.setToKey)
    def transpose(self):
        self.ui.textEdit.setText('transposed chords')
    def setFromKey(self, curr, prev):
        self.ui.textEdit.setText('fromKey set:' + curr.text())
    def setToKey(self):
        self.ui.textEdit.setText('toKey set')

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
