#!/usr/bin/env python

import sys
import signal #quit on CTRL-C

from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)

        #create window, set title, status bar
        screen = QtGui.QDesktopWidget().screenGeometry()
        self.resize(1280, 800)
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
        self.setWindowTitle('kongming')
        self.setWindowIcon(QtGui.QIcon('icons/web.png'))
        self.statusBar().showMessage('Ready')
        self.statusBar()

        #menu: exit
        exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        #create menu
        menubar = self.menuBar()
        mfile = menubar.addMenu('&File')
        mfile.addAction(exit)

        #create center widget
        center = mainwidget()
        self.setCentralWidget(center)

class mainwidget(QtGui.QTabWidget):
    def __init__(self, parent=None):
        QtGui.QTabWidget.__init__(self, parent)

        #create tabs
        bs = battlestation()
        self.addTab(bs, "Battlestation")
        tl = telemlist()
        self.addTab(tl, "Telemetry List")

#all nice GUIs and shit.
class battlestation(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)

        okbutton = QtGui.QPushButton("OK")

        col1 = QtGui.QVBoxLayout()
        col1.addWidget(okbutton)
        col1.addStretch(1)

        maincolumns = QtGui.QHBoxLayout()
        maincolumns.addLayout(col1)
        maincolumns.addStretch(1)
        self.setLayout(maincolumns)


# 4 columns, for node 0-63, 64-127, 128-192, 192-255
class telemlist(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)

        okbutton = QtGui.QPushButton("OK2")

        col1 = QtGui.QVBoxLayout()
        col1.addWidget(okbutton)
        col1.addStretch(1)

        maincolumns = QtGui.QHBoxLayout()
        maincolumns.addLayout(col1)
        maincolumns.addStretch(1)
        self.setLayout(maincolumns)

#constantly flowing telemetry stream, filtered
class telemfilter(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)

        okbutton = QtGui.QPushButton("OK3")

        col1 = QtGui.QVBoxLayout()
        col1.addWidget(okbutton)
        col1.addStretch(1)

        maincolumns = QtGui.QHBoxLayout()
        maincolumns.addLayout(col1)
        maincolumns.addStretch(1)
        self.setLayout(maincolumns)

app = QtGui.QApplication(sys.argv)
signal.signal(signal.SIGINT, signal.SIG_DFL)
kongming = MainWindow()
kongming.show()
sys.exit(app.exec_())


