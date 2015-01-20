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
        QtCore.QObject.connect(self.ui.transpose,QtCore.SIGNAL("clicked()"), self.transpose)
    def transpose(self):
        self.ui.textEdit.setText('transposed chords')

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
