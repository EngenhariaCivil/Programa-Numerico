'''
Created on 6 de abr de 2016

@author: manoe
'''
import math
import matplotlib.pyplot as plt

class Plotter(object):

    def __init__(self, expoentes = [], coeficientes = []):
        '''
        Constructor
        '''
        self.expoentes = expoentes
        self.coeficientes = coeficientes
        self.funcao = 0
        
        
                
        
        
    
    def escreveFuncao(self):
        plt.plot([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9], [1,4,9,16,25,36,49,64,81])
        plt.show()
            
    
    def valor(self, x):
        temp = []
        for i in self.expoentes:
            temp.append(math.pow(x, i))
            
        resp = 0
        j = 0
        for k in self.coeficientes:
            resp += temp[j]*k 
            j += 1
        
        return resp 
                


           
        
        
        
        
        
        
        
        
        
        