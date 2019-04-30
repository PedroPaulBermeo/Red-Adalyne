#Red Neural Artificial Adaline
#Programado por: Pedro Bermeo
#Ing. Sistemas - IA2
'''
Ejemplo con valores:

    | x1  | x2  | d  |
    -----------------
    | 1   | 1   | -1 |
    | 1   | -1  | 1  |
    | -1  | 1   | -1 |
    | -1  | -1  | -1 |

    W = [0.2, 0.2]
    θ = 0.2
    α = 0.2

'''

#%matplotlib inline
import numpy as np

import matplotlib.pyplot as pp

class Adalyne():
    def __init__(self):

        self.Matriz = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        self.W = np.array([0.2, 0.2])
        self.bias = 0.2
        self.alfa = 0.2
        self.delta = [-1, 1, -1, -1]

        self.contI = 0
        self.cont0 = 0
        self.estado = False

        self.sE2=[]
        self.sumaE2=0

        self.MatrizResutlados=[]

    def calular(self):

        while(self.estado == False):
            self.contI+=1
            self.cont = 0
            for i in self.Matriz:
                self.X = np.array(i)
                self.y = np.sum(np.multiply(self.X, self.W)) + self.bias
                ''''
                if (n < 0):
                    y = 0
                else:
                    y = 1
                '''


                #print("Entradas", self.X)
                #print("Salidas Deseada: ", self.delta[self.cont])
                self.error = self.delta[self.cont] - self.y

                #print("Salida Obtenida: ", self.y)
                #print("Error", self.error)
                self.delta1=[]
                for j in self.X:
                    self.delta1.append(self.alfa*self.error*j)

                self.delta1.append(self.alfa*self.error)
                #print("Deltas",self.delta1)
                #print("Pesos", self.W)
                #print("Beta",self.bias)
                self.error2=pow(self.error,2)
                self.sumaE2+=self.error2

                #print("Error 2",self.error2)
                lista=[]
                lista.append(self.X)
                #print("lista",lista)

                lista.append(self.delta[self.cont])
                self.cont += 1
                lista.append(self.y)
                lista.append(self.error)
                lista.append(self.delta1)
                if (self.error != 0):
                    cont0=0
                    #print("Actualiza pesos")
                    self.W = (self.W + np.multiply(self.alfa* self.error, self.X))
                    #print("Nuevo W", self.W)
                    self.bias = self.bias + (self.alfa * self.error)
                    #print("Nuevo bias", self.bias)
                    lista.append(self.W)
                    lista.append(self.bias)
                else:
                    lista.append(0)
                    lista.append(0)

                lista.append(self.error2)
                self.MatrizResutlados.append(lista)
                if (self.cont == 4):
                    self.sE2.append(self.sumaE2)
                    self.imprimirMatriz()
                    #print("Resultados Iteracion",MatrizResutlados)
                    #print("Suma Errores2", self.sumaE2)
                    self.sumaE2 = 0

                else:
                    cont0+=1

                    if(cont0==len(self.delta)):
                        print("Termino la Ejecucion. \n")
                        print("Pesos Finales",self.W)
                        print("Bias Final",self.bias)
                        self.estado=True
                        break

                #print("******************************\n")

    def imprimirMatriz(self):

        print("***********************************************************************************************************************************************************************")
        print("| Resultados Iteracion # ",self.contI,": |")
        print("|x1|  \t\t|x2| \t\t |d| \t\t\t|y| \t\t |e| \t\t\t|Δw1| \t\t\t  |Δw2| \t\t |Δθ| \t\t\t |w1| \t\t |w2| \t\t  |θ| \t\t  |Error^2|")
        for i in self.MatrizResutlados:
            wt = i[0]
            yt = str(i[2])
            bt = i[4]
            wtn = i[5]
            print(wt[0], "\t\t\t", wt[1],"\t\t\t",i[1],"\t\t  ",yt[:5],"\t\t",str(i[3])[:5],"\t\t  ",str(bt[0])[:5],"\t\t\t",str(bt[1])[:5],
                  "\t\t\t",str(bt[2])[:5],"\t\t\t",str(wtn[0])[:5],"\t\t",str(wtn[1])[:5],"\t\t",str(i[6])[:5],"\t\t  ",str(i[7])[:5])

        print("|Suma Errores ^2:", self.sumaE2, '|')

        if(len(self.sE2)>3):
            contr=0
            for i in self.sE2:
                n1=str(i)[:5]
                n2=str(self.sumaE2)[:5]
                #print("n1",n1)
                #print("n2", n1)

                if n1 == n2:
                    contr+=1

                    if(contr ==3):
                        print("Termino la Ejecucion. \n")
                        print("Pesos Finales", self.W)
                        print("Bias Final", self.bias)
                        self.crearGrafica()
                        self.estado = True
                        break


        print("***********************************************************************************************************************************************************************\n")
            #print(i)
        self.MatrizResutlados=[]

    def crearGrafica(self):
        x =list(range(1,len(self.sE2)+1))

        pp.plot(x, self.sE2, color="teal", linewidth=2.5, linestyle="-")
        pp.suptitle("Grafica de Error Total por Iteracion", color="teal")
        a = "Total de Iteraciones",(len(self.sE2)+1)
        pp.title(a, color='red')
        pp.plot(x, self.sE2, 'ro')
        #pp.plot(x, y, color="teal", linewidth=2.5, linestyle="-", label="a")
        pp.xlabel("#Iteracion", color="sienna")
        pp.ylabel("Sumatoria de Error", color="sienna")
        pp.legend(loc='upper center')
        pp.grid(True)
        # pp.set_title('Grafica Final')
        pp.savefig('grafico.png')
        pp.show()

if __name__ == '__main__':
    np.set_printoptions(precision=2, suppress=True)
    ada = Adalyne()
    ada.calular()