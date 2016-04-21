'''
Created on 6 de abr de 2016

@author: manoe
'''
#from Plotter import Plotter
from PyQt4 import QtCore, QtGui
from JanelaPrincipal import JanelaPrincipal

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QMainWindow()
    ui = JanelaPrincipal()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())

''' 
    p = Plotter([3,2,1,0],[1,-7,2,-3])
    print(p.valor(-3))
    p.escreveFuncao() 
    
    f = "(ln(x^(x+1)*lnx)-2^(2/x))/3"
'''
    
    
        #calcula y para x = 2 bla bla 
    #bla bla
    #primeiro teste
   # func = "math.sqrt((5 + 2)*2)"
   # print(eval(func))
    