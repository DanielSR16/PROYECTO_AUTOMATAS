datos = '( a 00, H )-( a 0 1 , H ,R)-( a 00, 1 )-( b 0 1 , 1 ,R)-( a 00, 2 )-( c 0 1 , 2 ,R)-( a 00, 3 )-( d 0 1 , 3 ,R)-( a 00, 4 )-( e 0 1 , 4 ,R)-( a 00, 5 )-( f 0 1 , 5 ,R)-( a00, 6 )-( g 0 7 , 6 ,R)-( a 00, 7 )-( h 0 8 , 7 ,R)-( a 00, 8 )-( i 0 9 , 8 ,R)-( a 00, 9 )-( j 0 10 , 9 ,R)-( a 00, 1 )-( k 0 11 , 1 ,R)-'
a = '(a01,b)-(a02,meta,R)-(a02,B)-(a02,B,S)-'

b = '(b01,0)-(b02,0,R)-(b01,1)-(b12,1,R)-(b01,2)-(b22,2,R)-(b01,3)-(b32,3,R)-(b01,4)-(b42,4,R)-(b01,5)-(b52,5,R)-(b01,6)-(b62,6,R)-(b01,7)-(b72,7,R)-(b01,8)-(b82,8,R)-(b01,9)-(b92,9,R)-(b14,B)-(b15,deca,R)-(b15,B)-(b15,B,S)-'
b1 = '(b12,H)-(b13,H,R)-(b22,H)-(b23,H,R)-(b32,H)-(b33,H,R)-(b42,H)-(b43,H,R)-(b52,H)-(b53,H,R)-(b62,H)-(b63,H,R)-(b72,H)-(b73,H,R)-(b82,H)-(b83,H,R)-(b92,H)-(b93,H,R)-(b02,H)-(b03,H,R)-(b03,B)-(b04,deca,R)-(b04,B)-(b04,B,S)-' 
b2 =  '(b13,B)-(b14,un,R)-(b23,B)-(b14,do,R)-(b33,B)-(b14,tri,R)-(b43,B)-(b14,tetra,R)-(b53,B)-(b14,penta,R)-(b63,B)-(b14,hexa,R)-(b73,B)-(b14,hepta,R)-(b83,B)-(b14,octa,R)-(b93,B)-(b14,nona,R)-'
c = '(c01,0)-(c02,0,R)-(c01,1)-(c12,1,R)-(c01,2)-(c22,2,R)-(c01,3)-(c32,3,R)-(c01,4)-(c42,4,R)-(c01,5)-(c52,5,R)-(c01,6)-(c62,6,R)-(c01,7)-(c72,7,R)-(c01,8)-(c82,8,R)-(c01,9)-(c92,9,R)-'
d = '(d01,0)-(d02,0,R)-(d01,1)-(d12,1,R)-(d01,2)-(d22,2,R)-(d01,3)-(d32,3,R)-(d01,4)-(d42,4,R)-(d01,5)-(d52,5,R)-(d01,6)-(d62,6,R)-(d01,7)-(d72,7,R)-(d01,8)-(d82,8,R)-(d01,9)-(d92,9,R)-'
e = '(e01,0)-(e02,0,R)-(e01,1)-(e12,1,R)-(e01,2)-(e22,2,R)-(e01,3)-(e32,3,R)-(e01,4)-(e42,4,R)-(e01,5)-(e52,5,R)-(e01,6)-(e62,6,R)-(e01,7)-(e72,7,R)-(e01,8)-(e82,8,R)-(e01,9)-(e92,9,R)-'
f = '(f01,0)-(f02,0,R)-(f01,1)-(f12,1,R)-(f01,2)-(f22,2,R)-(f01,3)-(f32,3,R)-(f01,4)-(f42,4,R)-(f01,5)-(f52,5,R)-(f01,6)-(f62,6,R)-(f01,7)-(f72,7,R)-(f01,8)-(f82,8,R)-(f01,9)-(f92,9,R)-'
g = '(g01,0)-(g02,0,R)-(g01,1)-(g12,1,R)-(g01,2)-(g22,2,R)-(g01,3)-(g32,3,R)-(g01,4)-(g42,4,R)-(g01,5)-(g52,5,R)-(g01,6)-(g62,6,R)-(g01,7)-(g72,7,R)-(g01,8)-(g82,8,R)-(g01,9)-(g92,9,R)-'
h = '(h01,0)-(h02,0,R)-(h01,1)-(h12,1,R)-(h01,2)-(h22,2,R)-(h01,3)-(h32,3,R)-(h01,4)-(h42,4,R)-(h01,5)-(h52,5,R)-(h01,6)-(h62,6,R)-(h01,7)-(h72,7,R)-(h01,8)-(h82,8,R)-(h01,9)-(h92,9,R)-'
i = '(i01,0)-(i02,0,R)-(i01,1)-(i12,1,R)-(i01,2)-(i22,2,R)-(i01,3)-(i32,3,R)-(i01,4)-(i42,4,R)-(i01,5)-(i52,5,R)-(i01,6)-(i62,6,R)-(i01,7)-(i72,7,R)-(i01,8)-(i82,8,R)-(i01,9)-(i92,9,R)-'
j = '(j01,0)-(j02,0,R)-(j01,1)-(j12,1,R)-(j01,2)-(j22,2,R)-(j01,3)-(j32,3,R)-(j01,4)-(j42,4,R)-(j01,5)-(j52,5,R)-(j01,6)-(j62,6,R)-(j01,7)-(j72,7,R)-(j01,8)-(j82,8,R)-(j01,9)-(j92,9,R)-'

datos = datos+a+b+b1+b2 +c+d+e+f+g+h+i+j 

datosNuevos = datos.replace(' ','')
# print(datosNuevos)
arrayAux = []
arrayAux2 = []
arrayCompleto = []
bandera = False
valor = ''
for i in datosNuevos:
    if(i != '-'):
        if(i != '(' ):
            if i != ',' and i != ')' :
                valor = valor +i
       
            if( i == ',' or i == ')'):
                
                arrayAux.append(valor)
                valor = ''
             
           
    elif(i == '-'):
        arrayCompleto.append(arrayAux)
        arrayAux = []
   
par = 0 
numerosReales = 1
transicionesIda = []
transicionesLlegada = []
bandera = False
for i in arrayCompleto:
    if(bandera == False):
        transicionesIda.append(i)
        bandera = True 
    elif bandera == True:
        transicionesLlegada.append(i)
        bandera = False
        
ejecucion = True
contadorTransiciones = 1
def llenarCinta(entrada):
    cinta = []
    nuevaEntrada = entrada[1:len(entrada)-1][:-1]
    print(nuevaEntrada)
    for i in nuevaEntrada:
        cinta.append(i)
    cinta.append('B')
    cinta.append('B')
    cinta.append('B')
    
    return cinta

def maquina(entrada):
    contadorCinta = 0
    cabezal = 'a00'
    cinta = llenarCinta(entrada)
    banderaMaquina =True
    print('entrada cinta: ',cinta)
    
    while(banderaMaquina == True):
        
        for i in range(len(transicionesIda)):
            if(cabezal == transicionesIda[i][0] and cinta[contadorCinta] == transicionesIda[i][1]):
                
                print(transicionesIda[i][0])
                print(transicionesIda[i][1])
                cabezal = transicionesLlegada[i][0]
                print('nuevo cabezal: ',cabezal)
                cinta[contadorCinta] = transicionesLlegada[i][1]
                
                if transicionesLlegada[i][2] == 'R':
                    
                    contadorCinta +=1
                elif transicionesLlegada[i][2] == 'S':
                    banderaMaquina = False
                
                print('si lo encontre')
                
                break
    print(cinta)           
            
    
    
# print(transicionesIda)
# print('_____________________________________________')
# print(transicionesLlegada)

# cinta = llenarCinta('C11H24')
# print(cinta)
maquina('C10H30')
