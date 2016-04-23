# -*- coding: utf-8 -*-


# Form implementation generated from reading ui file 'JanelaPrincipal3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as grafico
import parser
import math

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
    ######################    DEFINICAO DE VARIAVEIS    #######################################
    funcao = ""
    limiteXEsquerda = 0.001
    limiteXDireita = 150
    dicionarioBotoesEspeciais = {"math.e" : "E", \
                                 "math.asin(" : "arcsen(", \
                                 "math.acos(" : "arccos(", \
                                 "math.atan(" : "arctan(", \
                                 "math.sin(" : "sen(", \
                                 "math.cos(" : "cos(", \
                                 "math.tan(" : "tan(", \
                                 "math.pi" : "π", \
                                 "math.log10(" : "Log(", \
                                 "math.log(" : "Ln(", \
                                 "**" : "^", \
                                 "math.sqrt(" : "√(", \
                                 "*" : "×"}
                            
    ###########################################################################################    
    
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(450, 650)
        MainWindow.setMinimumSize(QtCore.QSize(450, 650))
        MainWindow.setMaximumSize(QtCore.QSize(450, 650))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.titulo = QtGui.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(0, 20, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName(_fromUtf8("titulo"))
        
        self.rotuloIntervalo = QtGui.QLabel(self.centralwidget)
        self.rotuloIntervalo.setGeometry(QtCore.QRect(40, 530, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rotuloIntervalo.setFont(font)
        self.rotuloIntervalo.setObjectName(_fromUtf8("rotuloIntervalo"))
        
        self.rotuloX = QtGui.QLabel(self.centralwidget)
        self.rotuloX.setGeometry(QtCore.QRect(245, 530, 91, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.rotuloX.setFont(font)
        self.rotuloX.setAlignment(QtCore.Qt.AlignCenter)
        self.rotuloX.setObjectName(_fromUtf8("rotuloX"))
        
        self.campoLimiteEsquerda = QtGui.QPlainTextEdit(self.centralwidget)
        self.campoLimiteEsquerda.setGeometry(QtCore.QRect(170, 525, 71, 31))
        self.campoLimiteEsquerda.setObjectName(_fromUtf8("campoLimiteEsquerda"))
        
        self.campoLimiteDireita = QtGui.QPlainTextEdit(self.centralwidget)
        self.campoLimiteDireita.setGeometry(QtCore.QRect(340, 525, 71, 31))
        self.campoLimiteDireita.setObjectName(_fromUtf8("campoLimiteDireita"))
        
        self.rotuloDigiteFuncao = QtGui.QLabel(self.centralwidget)
        self.rotuloDigiteFuncao.setGeometry(QtCore.QRect(0, 80, 451, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rotuloDigiteFuncao.setFont(font)
        self.rotuloDigiteFuncao.setAlignment(QtCore.Qt.AlignCenter)
        self.rotuloDigiteFuncao.setObjectName(_fromUtf8("rotuloDigiteFuncao"))
        
        self.rotuloOpcoes = QtGui.QLabel(self.centralwidget)
        self.rotuloOpcoes.setGeometry(QtCore.QRect(40, 473, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rotuloOpcoes.setFont(font)
        self.rotuloOpcoes.setObjectName(_fromUtf8("rotuloOpcoes"))
        
        self.opcoes = QtGui.QComboBox(self.centralwidget)
        self.opcoes.setGeometry(QtCore.QRect(170, 475, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opcoes.setFont(font)
        self.opcoes.setObjectName(_fromUtf8("opcoes"))
        self.opcoes.addItem(_fromUtf8(""))
        self.opcoes.addItem(_fromUtf8(""))
        self.opcoes.addItem(_fromUtf8(""))
        self.opcoes.addItem(_fromUtf8(""))
        self.opcoes.addItem(_fromUtf8(""))
        self.opcoes.addItem(_fromUtf8(""))
        
        self.ok = QtGui.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(190, 600, 80, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ok.setFont(font)
        self.ok.setObjectName(_fromUtf8("ok"))
        
        self.sinalPotenciacao = QtGui.QPushButton(self.centralwidget)
        self.sinalPotenciacao.setGeometry(QtCore.QRect(280, 170, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.sinalPotenciacao.setFont(font)
        self.sinalPotenciacao.setObjectName(_fromUtf8("sinalPotenciacao"))
        
        self.tangente = QtGui.QPushButton(self.centralwidget)
        self.tangente.setGeometry(QtCore.QRect(330, 320, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.tangente.setFont(font)
        self.tangente.setObjectName(_fromUtf8("tangente"))
        
        self.tres = QtGui.QPushButton(self.centralwidget)
        self.tres.setGeometry(QtCore.QRect(180, 320, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.tres.setFont(font)
        self.tres.setObjectName(_fromUtf8("tres"))
        
        self.oito = QtGui.QPushButton(self.centralwidget)
        self.oito.setGeometry(QtCore.QRect(130, 220, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.oito.setFont(font)
        self.oito.setObjectName(_fromUtf8("oito"))
        
        self.seno = QtGui.QPushButton(self.centralwidget)
        self.seno.setGeometry(QtCore.QRect(230, 320, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.seno.setFont(font)
        self.seno.setObjectName(_fromUtf8("seno"))
        
        self.sinalSoma = QtGui.QPushButton(self.centralwidget)
        self.sinalSoma.setGeometry(QtCore.QRect(80, 170, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.sinalSoma.setFont(font)
        self.sinalSoma.setObjectName(_fromUtf8("sinalSoma"))
        
        self.sinalDivisao = QtGui.QPushButton(self.centralwidget)
        self.sinalDivisao.setGeometry(QtCore.QRect(230, 170, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.sinalDivisao.setFont(font)
        self.sinalDivisao.setObjectName(_fromUtf8("sinalDivisao"))
        
        self.sinalSubtracao = QtGui.QPushButton(self.centralwidget)
        self.sinalSubtracao.setGeometry(QtCore.QRect(130, 170, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.sinalSubtracao.setFont(font)
        self.sinalSubtracao.setObjectName(_fromUtf8("sinalSubtracao"))
        
        self.ponto = QtGui.QPushButton(self.centralwidget)
        self.ponto.setGeometry(QtCore.QRect(130, 370, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ponto.setFont(font)
        self.ponto.setObjectName(_fromUtf8("ponto"))
        
        self.um = QtGui.QPushButton(self.centralwidget)
        self.um.setGeometry(QtCore.QRect(80, 320, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.um.setFont(font)
        self.um.setObjectName(_fromUtf8("um"))
        
        self.arcoTangente = QtGui.QPushButton(self.centralwidget)
        self.arcoTangente.setGeometry(QtCore.QRect(330, 370, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(8)
        self.arcoTangente.setFont(font)
        self.arcoTangente.setObjectName(_fromUtf8("arcoTangente"))
        
        self.logNatural = QtGui.QPushButton(self.centralwidget)
        self.logNatural.setGeometry(QtCore.QRect(330, 220, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.logNatural.setFont(font)
        self.logNatural.setObjectName(_fromUtf8("logNatural"))
        
        self.nove = QtGui.QPushButton(self.centralwidget)
        self.nove.setGeometry(QtCore.QRect(180, 220, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.nove.setFont(font)
        self.nove.setObjectName(_fromUtf8("nove"))
        
        self.zero = QtGui.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(80, 370, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.zero.setFont(font)
        self.zero.setObjectName(_fromUtf8("zero"))
        
        self.arcoSeno = QtGui.QPushButton(self.centralwidget)
        self.arcoSeno.setGeometry(QtCore.QRect(230, 370, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(8)
        self.arcoSeno.setFont(font)
        self.arcoSeno.setObjectName(_fromUtf8("arcoSeno"))
        
        self.logBaseDez = QtGui.QPushButton(self.centralwidget)
        self.logBaseDez.setGeometry(QtCore.QRect(280, 220, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.logBaseDez.setFont(font)
        self.logBaseDez.setObjectName(_fromUtf8("logBaseDez"))
        
        self.dois = QtGui.QPushButton(self.centralwidget)
        self.dois.setGeometry(QtCore.QRect(130, 320, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.dois.setFont(font)
        self.dois.setObjectName(_fromUtf8("dois"))
        
        self.cosseno = QtGui.QPushButton(self.centralwidget)
        self.cosseno.setGeometry(QtCore.QRect(280, 320, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.cosseno.setFont(font)
        self.cosseno.setObjectName(_fromUtf8("cosseno"))
        
        self.botaoDelete = QtGui.QPushButton(self.centralwidget)
        self.botaoDelete.setGeometry(QtCore.QRect(230, 220, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botaoDelete.setFont(font)
        self.botaoDelete.setObjectName(_fromUtf8("botaoDelete"))
        
        self.quatro = QtGui.QPushButton(self.centralwidget)
        self.quatro.setGeometry(QtCore.QRect(80, 270, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.quatro.setFont(font)
        self.quatro.setObjectName(_fromUtf8("quatro"))
        
        self.sinalMultiplicacao = QtGui.QPushButton(self.centralwidget)
        self.sinalMultiplicacao.setGeometry(QtCore.QRect(180, 170, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.sinalMultiplicacao.setFont(font)
        self.sinalMultiplicacao.setObjectName(_fromUtf8("sinalMultiplicacao"))
        
        self.sete = QtGui.QPushButton(self.centralwidget)
        self.sete.setGeometry(QtCore.QRect(80, 220, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.sete.setFont(font)
        self.sete.setObjectName(_fromUtf8("sete"))
        
        self.parentesisAberto = QtGui.QPushButton(self.centralwidget)
        self.parentesisAberto.setGeometry(QtCore.QRect(230, 270, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.parentesisAberto.setFont(font)
        self.parentesisAberto.setObjectName(_fromUtf8("parentesisAberto"))
        
        self.seis = QtGui.QPushButton(self.centralwidget)
        self.seis.setGeometry(QtCore.QRect(180, 270, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.seis.setFont(font)
        self.seis.setObjectName(_fromUtf8("seis"))
        
        self.sinalRaizQuadrada = QtGui.QPushButton(self.centralwidget)
        self.sinalRaizQuadrada.setGeometry(QtCore.QRect(330, 170, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.sinalRaizQuadrada.setFont(font)
        self.sinalRaizQuadrada.setObjectName(_fromUtf8("sinalRaizQuadrada"))
        
        self.cinco = QtGui.QPushButton(self.centralwidget)
        self.cinco.setGeometry(QtCore.QRect(130, 270, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.cinco.setFont(font)
        self.cinco.setObjectName(_fromUtf8("cinco"))
        
        self.parentesisFechado = QtGui.QPushButton(self.centralwidget)
        self.parentesisFechado.setGeometry(QtCore.QRect(280, 270, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.parentesisFechado.setFont(font)
        self.parentesisFechado.setObjectName(_fromUtf8("parentesisFechado"))
        
        self.arcoCosseno = QtGui.QPushButton(self.centralwidget)
        self.arcoCosseno.setGeometry(QtCore.QRect(280, 370, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(8)
        self.arcoCosseno.setFont(font)
        self.arcoCosseno.setObjectName(_fromUtf8("arcoCosseno"))
        
        self.campoFuncao = QtGui.QLineEdit(self.centralwidget)
        self.campoFuncao.setGeometry(QtCore.QRect(25, 110, 400, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(13)
        self.campoFuncao.setFont(font)
        self.campoFuncao.setObjectName(_fromUtf8("campoFuncao"))
        
        self.numeroEuler = QtGui.QPushButton(self.centralwidget)
        self.numeroEuler.setGeometry(QtCore.QRect(180, 370, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.numeroEuler.setFont(font)
        self.numeroEuler.setObjectName(_fromUtf8("numeroEuler"))
        
        self.numPi = QtGui.QPushButton(self.centralwidget)
        self.numPi.setGeometry(QtCore.QRect(330, 270, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        self.numPi.setFont(font)
        self.numPi.setObjectName(_fromUtf8("numPi"))
        
        self.variavelX = QtGui.QPushButton(self.centralwidget)
        self.variavelX.setGeometry(QtCore.QRect(205, 420, 40, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria Math"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.variavelX.setFont(font)
        self.variavelX.setWhatsThis(_fromUtf8(""))
        self.variavelX.setObjectName(_fromUtf8("variavelX"))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ##################   CONECTANDO EVENTOS OCORRIDOS NA INTERFACE GRÁFICA   ##################
        ####################   COM OS METODOS A SEREM EXECUTADOS NO CODIGO   ######################
               
        self.campoFuncao.textChanged.connect(lambda: self.organizaFuncao()) #Pega o texto que o usuario
                                                                            #digita direto no campo de texto
                                                                            #com o teclado do pc 
        
        self.ok.clicked.connect(lambda: self.aplicaMetodo()) #Quando o botao OK recebe um clique
                                                             #o metodo encolhaDeMetodo eh chamado
        
        '''
        Codigo dos botoes
        '''    
        self.zero.clicked.connect(lambda: self.escreveFuncao("0"))   
        self.um.clicked.connect(lambda: self.escreveFuncao("1")) 
        self.dois.clicked.connect(lambda: self.escreveFuncao("2")) 
        self.tres.clicked.connect(lambda: self.escreveFuncao("3")) 
        self.quatro.clicked.connect(lambda: self.escreveFuncao("4")) 
        self.cinco.clicked.connect(lambda: self.escreveFuncao("5")) 
        self.seis.clicked.connect(lambda: self.escreveFuncao("6")) 
        self.sete.clicked.connect(lambda: self.escreveFuncao("7"))
        self.oito.clicked.connect(lambda: self.escreveFuncao("8")) 
        self.nove.clicked.connect(lambda: self.escreveFuncao("9")) 
        
        self.ponto.clicked.connect(lambda: self.escreveFuncao("."))
        self.seno.clicked.connect(lambda: self.escreveFuncao("math.sin(")) 
        self.cosseno.clicked.connect(lambda: self.escreveFuncao("math.cos(")) 
        self.tangente.clicked.connect(lambda: self.escreveFuncao("math.tan(")) 
        self.arcoSeno.clicked.connect(lambda: self.escreveFuncao("math.asin(")) 
        self.arcoCosseno.clicked.connect(lambda: self.escreveFuncao("math.acos(")) 
        self.arcoTangente.clicked.connect(lambda: self.escreveFuncao("math.atan(")) 
        self.numeroEuler.clicked.connect(lambda: self.escreveFuncao("math.e")) 
        self.parentesisAberto.clicked.connect(lambda: self.escreveFuncao("(")) 
        self.parentesisFechado.clicked.connect(lambda: self.escreveFuncao(")")) 
        self.numPi.clicked.connect(lambda: self.escreveFuncao("math.pi")) 
        self.logNatural.clicked.connect(lambda: self.escreveFuncao("math.log("))
        self.logBaseDez.clicked.connect(lambda: self.escreveFuncao("math.log10("))
        self.sinalRaizQuadrada.clicked.connect(lambda: self.escreveFuncao("math.sqrt(")) 
        self.sinalSoma.clicked.connect(lambda: self.escreveFuncao("+"))
        self.sinalSubtracao.clicked.connect(lambda: self.escreveFuncao("-"))
        self.sinalMultiplicacao.clicked.connect(lambda: self.escreveFuncao("*"))
        self.sinalDivisao.clicked.connect(lambda: self.escreveFuncao("/"))
        
        self.variavelX.clicked.connect(lambda: self.escreveFuncao("x"))
        self.botaoDelete.clicked.connect(lambda: self.escreveFuncao("DEL"))
        self.sinalPotenciacao.clicked.connect(lambda: self.escreveFuncao("**"))
        
             
        ############################################################################################
        
        
    #######################   METODOS INTERNOS NO PROGRAMA   #######################################  
    
    '''
    Exibeno campo de texto a string texto passada como parametro.
    '''
    def escreveFuncao(self, texto):
        print("I texto ->  " + texto)
        
        if texto == "DEL":
            self.campoFuncao.backspace()
        elif texto in self.dicionarioBotoesEspeciais:
            simbolo = self.dicionarioBotoesEspeciais[texto]
            self.campoFuncao.insert(simbolo)
        elif texto == "x" or texto == "X":
            self.campoFuncao.insert("X")
        else: 
            self.campoFuncao.insert(texto)

        print("Esc fun => " + self.funcao)
        
    '''
    Substitui todos os simbolos matematicos da string self.funcao, que 
    guarda a funcao matematica e que está exatamente como o usuario vê
    no campo de texto, numa string igual a um código python.
    Ex: Se  self.funcao = π  esse metodo a transforma em math.pi.
    Dessa forma é possivel transforma-la em codigo python. 
    '''    
    def organizaFuncao(self):
        listaSimbolos = []
        self.funcao = self.campoFuncao.text()
        
        
        for chave in self.dicionarioBotoesEspeciais:
            simbolo = self.dicionarioBotoesEspeciais[chave]
            listaSimbolos.append(simbolo)
            
        for simb in listaSimbolos:
            if simb in self.funcao:
                for chave2 in self.dicionarioBotoesEspeciais:
                    if simb == self.dicionarioBotoesEspeciais[chave2]:
                        self.funcao = self.funcao.replace(simb, chave2)
        
        print("Org fun => " + self.funcao)
    
    '''
    Transforma uma linha de codigo python que está no
    formato de string em codigo python mesmo.
    '''
    def transformaEmCodigoPy(self, texto):
        expressao = parser.expr(texto) 
        codigoExpresao = expressao.compile()
        return codigoExpresao    
         
    '''
    Plota o grafico da funcao que o usuario digitou no campo de texto.
    '''    
    def plotarGrafico(self):
        self.organizaFuncao()
        codigoPyFuncao = self.transformaEmCodigoPy(self.funcao) 
                                     
        if self.campoLimiteEsquerda.toPlainText() != "":                        #Esses IFs aplica o intervalo que o usuario
            self.limiteXEsquerda = float(self.campoLimiteEsquerda.toPlainText())#informou na interface grafica
        if self.campoLimiteDireita.toPlainText() != "":
            self.limiteXDireita = float(self.campoLimiteDireita.toPlainText())
            
        precisao = 0.001
        X = self.limiteXEsquerda + precisao #Esse X eh a variavel da minha funcao matematica, que foi 
        xs = []                             #digitada pelo usuario na interface e que eu transformei em
        ys = []                             #codigo python (que esta armazeanado na variavel codigoExpressao)
        
        while X > self.limiteXEsquerda and X < self.limiteXDireita:
            xs.append(X)
            ys.append(eval(codigoPyFuncao)) #Esse eval() avalia (calcula) valor de f(X) 
            
            X += precisao
            
        grafico.plot(xs, ys)        
        grafico.show()
        
        
    def aplicaMetodo(self):
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
        
        ###################################################################################################


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Metodos Numéricos", None))
        self.titulo.setText(_translate("MainWindow", "Métodos Numéricos", None))
        self.rotuloIntervalo.setText(_translate("MainWindow", "Defina um intervalo", None))
        self.rotuloX.setText(_translate("MainWindow", "<   X   <", None))
        self.rotuloDigiteFuncao.setText(_translate("MainWindow", "Digite uma função", None))
        self.rotuloOpcoes.setText(_translate("MainWindow", "Escolha o método", None))
        self.opcoes.setItemText(0, _translate("MainWindow", "Euler", None))
        self.opcoes.setItemText(1, _translate("MainWindow", "Runge Kutta", None))
        self.opcoes.setItemText(2, _translate("MainWindow", "Taylor", None))
        self.opcoes.setItemText(3, _translate("MainWindow", "Trapézio", None))
        self.opcoes.setItemText(4, _translate("MainWindow", "Simpson", None))
        self.opcoes.setItemText(5, _translate("MainWindow", "Newton-Raphson", None))
        self.ok.setText(_translate("MainWindow", "OK", None))
        self.sinalPotenciacao.setText(_translate("MainWindow", "^", None))
        self.tangente.setText(_translate("MainWindow", "tan", None))
        self.tres.setText(_translate("MainWindow", "3", None))
        self.oito.setText(_translate("MainWindow", "8", None))
        self.seno.setText(_translate("MainWindow", "sen", None))
        self.sinalSoma.setText(_translate("MainWindow", "+", None))
        self.sinalDivisao.setText(_translate("MainWindow", "/", None))
        self.sinalSubtracao.setText(_translate("MainWindow", "-", None))
        self.ponto.setText(_translate("MainWindow", ".", None))
        self.um.setText(_translate("MainWindow", "1", None))
        self.arcoTangente.setText(_translate("MainWindow", "arctan", None))
        self.logNatural.setText(_translate("MainWindow", "ln", None))
        self.nove.setText(_translate("MainWindow", "9", None))
        self.zero.setText(_translate("MainWindow", "0", None))
        self.arcoSeno.setText(_translate("MainWindow", "arcsen", None))
        self.logBaseDez.setText(_translate("MainWindow", "log", None))
        self.dois.setText(_translate("MainWindow", "2", None))
        self.cosseno.setText(_translate("MainWindow", "cos", None))
        self.botaoDelete.setText(_translate("MainWindow", "DEL", None))
        self.quatro.setText(_translate("MainWindow", "4", None))
        self.sinalMultiplicacao.setText(_translate("MainWindow", "×", None))
        self.sete.setText(_translate("MainWindow", "7", None))
        self.parentesisAberto.setText(_translate("MainWindow", "(", None))
        self.seis.setText(_translate("MainWindow", "6", None))
        self.sinalRaizQuadrada.setText(_translate("MainWindow", "√", None))
        self.cinco.setText(_translate("MainWindow", "5", None))
        self.parentesisFechado.setText(_translate("MainWindow", ")", None))
        self.arcoCosseno.setText(_translate("MainWindow", "arccos", None))
        self.numeroEuler.setText(_translate("MainWindow", "e", None))
        self.numPi.setText(_translate("MainWindow", "π", None))
        self.variavelX.setText(_translate("MainWindow", "X", None))

