# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janelaPrincipal.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as grafico

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

class JanelaPrincipal(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(453, 353)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.titulo = QtGui.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(60, 20, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName(_fromUtf8("titulo"))
        
        self.rotuloIntervalo = QtGui.QLabel(self.centralwidget)
        self.rotuloIntervalo.setGeometry(QtCore.QRect(20, 210, 111, 16))
        self.rotuloIntervalo.setObjectName(_fromUtf8("rotuloIntervalo"))
        
        self.rotuloX = QtGui.QLabel(self.centralwidget)
        self.rotuloX.setGeometry(QtCore.QRect(195, 210, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.rotuloX.setFont(font)
        self.rotuloX.setAlignment(QtCore.Qt.AlignCenter)
        self.rotuloX.setObjectName(_fromUtf8("rotuloX"))
        
        self.limiteEsquerda = QtGui.QPlainTextEdit(self.centralwidget)
        self.limiteEsquerda.setGeometry(QtCore.QRect(120, 205, 71, 31))
        self.limiteEsquerda.setObjectName(_fromUtf8("limiteEsquerda"))
        
        self.limiteDireita = QtGui.QPlainTextEdit(self.centralwidget)
        self.limiteDireita.setGeometry(QtCore.QRect(290, 205, 71, 31))
        self.limiteDireita.setObjectName(_fromUtf8("limiteDireita"))
        
        self.rotuloDigiteFuncao = QtGui.QLabel(self.centralwidget)
        self.rotuloDigiteFuncao.setGeometry(QtCore.QRect(20, 95, 81, 16))
        self.rotuloDigiteFuncao.setObjectName(_fromUtf8("rotuloDigiteFuncao"))
        
        self.campoFuncao = QtGui.QPlainTextEdit(self.centralwidget)
        self.campoFuncao.setGeometry(QtCore.QRect(120, 90, 241, 31))
        self.campoFuncao.setObjectName(_fromUtf8("campoFuncao"))
        
        self.rotuloOpcoes = QtGui.QLabel(self.centralwidget)
        self.rotuloOpcoes.setGeometry(QtCore.QRect(20, 153, 91, 16))
        self.rotuloOpcoes.setObjectName(_fromUtf8("rotuloOpcoes"))
        
        self.opcoes = QtGui.QComboBox(self.centralwidget)
        self.opcoes.setGeometry(QtCore.QRect(120, 150, 111, 22))
        self.opcoes.setObjectName(_fromUtf8("opcoes"))
        self.opcoes.addItem(_fromUtf8(""))
        self.opcoes.addItem(_fromUtf8(""))
        self.opcoes.addItem(_fromUtf8(""))
        self.opcoes.addItem(_fromUtf8(""))
        self.opcoes.addItem(_fromUtf8(""))
        self.opcoes.addItem(_fromUtf8(""))
        
        self.ok = QtGui.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(190, 280, 75, 23))
        self.ok.setObjectName(_fromUtf8("ok"))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        
        self.ok.clicked.connect(lambda: self.escolhaDeMetodo()) #Quando o botao OK eh recebe um clique
                                                                #o metodo encolhaDeMetodo eh chamado

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Metodos Numéricos", None))
        self.titulo.setText(_translate("MainWindow", "Métodos Numéricos", None))
        self.rotuloIntervalo.setText(_translate("MainWindow", "Defina um intervalo", None))
        self.rotuloX.setText(_translate("MainWindow", "<   X   <", None))
        self.rotuloDigiteFuncao.setText(_translate("MainWindow", "Digite a Função", None))
        self.rotuloOpcoes.setText(_translate("MainWindow", "Escolha o método", None))
        self.opcoes.setItemText(0, _translate("MainWindow", "Euler", None))
        self.opcoes.setItemText(1, _translate("MainWindow", "Runge Kutta", None))
        self.opcoes.setItemText(2, _translate("MainWindow", "Taylor", None))
        self.opcoes.setItemText(3, _translate("MainWindow", "Trapézio", None))
        self.opcoes.setItemText(4, _translate("MainWindow", "Simpson", None))
        self.opcoes.setItemText(5, _translate("MainWindow", "Newton-Raphson", None))
        self.ok.setText(_translate("MainWindow", "OK", None))
    
    
    def plotarGrafico(self):
        grafico.plot([1,2,3,4,5,6,7,8,9], [1,4,9,16,25,36,49,64,81])
        grafico.show()
        
    def escolhaDeMetodo(self):
        metodo = self.opcoes.currentText()
        
        if metodo == "Euler":
            print("Euler")
        elif metodo == "Runge Kutta":
            print("Runge Kutta")
        elif metodo == "Simpson":
            print("Simpson")
        elif metodo == "Taylor":
            print("Taylor")
        elif metodo == "Trapézio":
            print("Trapezio")
        else:
            pass
        
        self.plotarGrafico()

'''
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QMainWindow()
    ui = JanelaPrincipal()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
'''