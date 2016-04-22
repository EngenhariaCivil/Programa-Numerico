'''
Created on 6 de abr de 2016

@author: manoe
'''
#from Plotter import Plotter
from PyQt4 import QtCore, QtGui
from JanelaPrincipal import JanelaPrincipal
import parser
import math

if __name__ == '__main__':
    
    import sys
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QMainWindow()
    ui = JanelaPrincipal()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())

    