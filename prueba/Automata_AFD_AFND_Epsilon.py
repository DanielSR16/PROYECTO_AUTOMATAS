from os import terminal_size
from sys import path
from typing import Final
import tkinter as tk

from datos import Q,S,F,D

archivo = open('datos.txt','r')


# lista = archivo.readline().replace(' ','')
# Q = lista
# lista = archivo.readline().replace(' ','')
# S = lista
# lista = archivo.readline().replace(' ','')
# F = lista
# lista = archivo.readline().replace(' ','')
# q0 = lista
# lista = archivo.readline().replace(' ','')
# D = lista


q0 = 'q0={q0}'
  
def verificacionLlaves(cadena):
    epsilon = False
    tipoDeAutomata = 'AFD'
    contador=0
    conexionesAux = ""
    for i in range (3,len(D)):
        if(D[i] != "(" and D[i] != ")" and  D[i] != "\n"): 
            if(i != len(D)-2):
                conexionesAux = conexionesAux + D[i]     
    conexionesAuxList = conexionesAux.split(',')

    # print(conexionesAuxList)
    for valores in conexionesAuxList:
     
        if(valores.count('{')>=1 or valores.count('}')):
            tipoDeAutomata = 'AFND'
    
    for valoresE in conexionesAuxList:
        if valoresE.count('epsilon') >= 1:
            epsilon = True 
    if tipoDeAutomata == 'AFND' and epsilon == True:
        print('soy EPSILON')
        resultado = AFNDEpsilon(conexiones3(D),cadena)
    elif tipoDeAutomata == 'AFND':
        print('soy AFND')
        resultado = AFND(conexiones3(D),cadena)
       
    elif tipoDeAutomata == 'AFD':
        print('soy AFD')
        resultado = AFND(conexiones(D),cadena)
    return  resultado   
   
        

def conexiones(D):
    conexiones_D = [[],[],[]]
    contador = 1
    listAux =[]
    conexionesAux = ""
    for i in range (2,len(D)):
        if(D[i] != "{" and D[i] != "}" and D[i] != "(" and D[i] != ")" and  D[i] != "\n"):   
            conexionesAux = conexionesAux + D[i]

    conexionesAuxList = conexionesAux.split(',')
    for i in conexionesAuxList:
        if(contador == 1):
            conexiones_D[0].append(i)
            contador = 2
        elif(contador == 2):
            conexiones_D[1].append(i)
            contador = 3
        elif(contador == 3):
            listAux.append(i)
            conexiones_D[2].append(listAux)
            listAux = []
            contador = 1
    return conexiones_D

def conexiones3(D):
    conexiones_D = [[],[],[]]
    conexionesAux = ""
    aux2 = ''
    conta = 0
    for i in range (3,len(D)):
        if(D[i] != "(" and D[i] != ")" and  D[i] != "\n"): 
            if(i != len(D)-2):
                conexionesAux = conexionesAux + D[i]
    print('_________________________________')
    print(conexionesAux)
    print('___________________________')
    conexionesAuxList = conexionesAux.split(',')
    listAux = []
    for i in conexionesAuxList:
        if(conta==0):
            conexiones_D[conta].append(i)
            conta = 1
        elif(conta == 1):
            conexiones_D[conta].append(i)
            conta = 2
        elif(conta == 2):      
            conta = 2
            if('{' in i and '}' in i):
                auxEstadoAbiertoCerrado = i.replace('{','').replace('}','')
                listAux.append(auxEstadoAbiertoCerrado)
                conexiones_D[conta].append(listAux)
                aux2 = ''
                listAux = []
                conta = 0          
            elif '{' in i :
                auxEstadoAbierto = i.replace('{','')
                #print('remplaze cerrado }: ',auxEstadocerrado)
                aux2 =  aux2+ auxEstadoAbierto+','          
            elif '}' in i :
                auxEstadoCerrado = i.replace('}',"")
                aux2 = aux2 + auxEstadoCerrado
                listAux.append(aux2)
                conexiones_D[conta].append(listAux)
                listAux = []
                aux2 = ''
                conta = 0
                
            else:
                aux2 = aux2 + i +','
               
    listAuxiliar = []
    for x in range(0,len(conexiones_D[2])):
        #print((conexiones_D[2][x]))
        auxiliar = conexiones_D[2][x][0].split(',')
        listAuxiliar.append(auxiliar)
    conexiones_D[2] = listAuxiliar
    return conexiones_D
            
def estados(Q):
    estadosAux = ""
    for i in range (2,len(Q)):
        if(Q[i] != "{" and Q[i] != "}" and Q[i] != '\n'):
            estadosAux = estadosAux + Q[i]         
    estadosAuxLista = estadosAux.split(',')
    return estadosAuxLista
    
def alfabeto(S):
    alfabetoAux = ""
    for i in range (2,len(S)):
        if(S[i] != "{" and S[i] != "}" and S[i] != "\n"):
            alfabetoAux = alfabetoAux + S[i]         
    alfabetoAuxLista = alfabetoAux.split(',')
    return alfabetoAuxLista

def inicio(q0):
    inicioAux = ""
    for i in range (3,len(q0)):
        if(q0[i] != "{" and q0[i] != "}" and q0[i] != "\n"):
            inicioAux = inicioAux + q0[i]         
    inicioAuxLista = inicioAux.split(',')
    return inicioAuxLista   

def final(F):
    finalAux = ""
    for i in range (2,len(F)):
        if(F[i] != "{" and F[i] != "}" and F[i] != "\n"):
            finalAux = finalAux + F[i]         
    finalAuxLista = finalAux.split(',')

    return finalAuxLista 


def AFND(ListaPadre,cadena):

    auxEstado = [] 
    auxEstado = inicio(q0)
    bandera = True
    band = False
    
    for i in range(0,len(cadena)):
        band = False
        if(cadena[i] in alfabeto(S)): #if si existe el valor dentro del alfabeto
            letra = cadena[i] 
            for a in range(0,len(ListaPadre[1])): #recorre todas las variables que se encuentran en D ejemplo ['a', 'c', 'c', 'b', 'c'] 

                if(ListaPadre[1][a] == letra): #if la variable de la lista es igual a la variable de la entrada a averificar pasa
                    
                    for aux in auxEstado:  
                        if(ListaPadre[0][a] == aux):
                            auxEstado = ListaPadre[2][a]
                            letra = ""   
                            print(auxEstado)    
                            band = True

        else:
            ImpresionFinal = 'Cadena Invalida'
            bandera = False 
    if(bandera == True):
        if(band == True):
            for ultimo in auxEstado:
                    print(ultimo)
                    if(ultimo in final(F) ):
                        ImpresionFinal= 'Cadena Valida'
                        break
                    else:
                        ImpresionFinal = 'Cadena Invalida'
                        
        else:
            ImpresionFinal = 'Cadena Invalida'
    return ImpresionFinal




def AFNDEpsilon(listaPadre,cadena):
    bandera = False
    estado = []
    estado = inicio(q0)
    contador = 0
    
    while(bandera == False):
        encontreNormal = False
        encontreEpsilon = False
        banderaFinal =  False
        
        if contador <= len(cadena)-1:
            letra = cadena[contador]
            banderaTipo = 'letra'
        else:
            banderaTipo = 'epsilon'
            letra = 'epsilon'
        if letra in alfabeto(S):

            if banderaTipo == 'letra':
                    for i in range(0,len(listaPadre[0])):
                          for valor in estado:
                            if valor == listaPadre[0][i]:
                                if letra == listaPadre[1][i]:
                                  
                                    estado = listaPadre[2][i]
                                    
                                    letra=''
                                    contador +=1
                                    
                                    encontreNormal = True
                                    
                    letra=''
                   
                   
            if encontreNormal == False:
                letra = 'epsilon'
                for i in range(0,len(listaPadre[0])):
                    for valor in estado:   
                        if valor == listaPadre[0][i]:
                            if letra == listaPadre[1][i]:
                                letra=''
                             
                                estado = listaPadre[2][i]
                             
                                encontreEpsilon = True
                                
                letra=''
            for i in estado:                 
                    if i in final(F):
                       
                        banderaFinal = True
            if encontreEpsilon == False and encontreNormal == False:
         
                bandera= True
                return 'Cadena Invalida'
               
            elif(len(cadena) <= contador and banderaFinal == True): 
                        
                        bandera= True
                        return 'Cadena Valida'
                        
        else:
     
           bandera = True
           return 'Cadena Invalida'
                



root= tk.Tk()
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

label1 = tk.Label(root, text='Automatas Finitos')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Ingrese una cadena')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

ecuacion = 'C83H168'
numeros = ['1','2','3','4','5','6','7','8','9','0']
bandera = False
entreAvalidar = False
aux = []
entradaFinal = [[],[],[],[]]
tipoDatos = ['C','H']
for i in ecuacion:
    if(i == 'C'):
        entradaFinal[0].append(i)
    elif(i in numeros and bandera == False):
        entradaFinal[1].append(i)
        entreAvalidar = True
    elif(i == 'H'):
        entradaFinal[2].append(i)
        bandera = True
    elif(i in numeros and bandera == True):
        entradaFinal[3].append(i)
datoAux1 = ''
datoAux2 = ''
for i in entradaFinal[1]:
    datoAux1 = datoAux1 + i
for x in entradaFinal[3]:
    datoAux2 = datoAux2 + x

entradaFinal[1] = []
entradaFinal[1].append(datoAux1)
entradaFinal[3] = []
entradaFinal[3].append(datoAux2)

if(entreAvalidar == False):
    entradaFinal[1]= []
    entradaFinal[1].append('vacio')
    for i in entradaFinal:
        if(i[0] == 'vacio'):
            entradaFinal.pop(entradaFinal.index(i))
      

auxEntrada = []
for i in entradaFinal:
    auxEntrada.append(i[0])
entradaFinal = []
entradaFinal = auxEntrada
print(entradaFinal)  
    
# print(estados(Q))
# print()
# print(alfabeto(S))
# print()
# print(inicio(q0))
# print()

# print(final(F))
# print()
# print(conexiones3(D))
# print(D)
a = verificacionLlaves(entradaFinal)
print(a)
