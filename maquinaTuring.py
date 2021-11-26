datos = '( a 00, H )-( a 0 1 , H ,R)-( a 00, 1 )-( b 0 1 , 1 ,R)-( a 00, 2 )-( c 0 1 , 2 ,R)-( a 00, 3 )-( d 0 1 , 3 ,R)-( a 00, 4 )-( e 0 1 , 4 ,R)-( a 00, 5 )-( f 0 1 , 5 ,R)-( a00, 6 )-( g 0 1 , 6 ,R)-( a 00, 7 )-( h 0 1 , 7 ,R)-( a 00, 8 )-( i 0 1 , 8 ,R)-( a 00, 9 )-( j 0 1 , 9 ,R)-( a 00, 1 )-( k 0 11 , 1 ,R)-'
a = '(a01,B)-(a02,meta,R)-(a02,B)-(a02,B,S)-'

b = '(b01,0)-(b02,0,R)-(b01,1)-(b12,1,R)-(b01,2)-(b22,2,R)-(b01,3)-(b32,3,R)-(b01,4)-(b42,4,R)-(b01,5)-(b52,5,R)-(b01,6)-(b62,6,R)-(b01,7)-(b72,7,R)-(b01,8)-(b82,8,R)-(b01,9)-(b92,9,R)-(b14,B)-(b15,deca,R)-(b15,B)-(b15,B,S)-'
b1 = '(b12,H)-(b13,H,R)-(b22,H)-(b23,H,R)-(b32,H)-(b33,H,R)-(b42,H)-(b43,H,R)-(b52,H)-(b53,H,R)-(b62,H)-(b63,H,R)-(b72,H)-(b73,H,R)-(b82,H)-(b83,H,R)-(b92,H)-(b93,H,R)-(b02,H)-(b03,H,R)-(b03,B)-(b04,deca,R)-(b04,B)-(b04,B,S)-(b02,0)-(b05,0,R)-(b05,H)-(b06,H,R)-(b06,B)-(b07,hecta,R)-(b07,B)-(b07,B,S)-' 
b2 =  '(b13,B)-(b14,un,R)-(b23,B)-(b14,do,R)-(b33,B)-(b14,tri,R)-(b43,B)-(b14,tetra,R)-(b53,B)-(b14,penta,R)-(b63,B)-(b14,hexa,R)-(b73,B)-(b14,hepta,R)-(b83,B)-(b14,octa,R)-(b93,B)-(b14,nona,R)-'

c = '(c01,H)-(C02,H,R)-(c01,0)-(c02,0,R)-(c01,1)-(c12,1,R)-(c01,2)-(c22,2,R)-(c01,3)-(c32,3,R)-(c01,4)-(c42,4,R)-(c01,5)-(c52,5,R)-(c01,6)-(c62,6,R)-(c01,7)-(c72,7,R)-(c01,8)-(c82,8,R)-(c01,9)-(c92,9,R)-(c04,B)-(c04,B,S)-(c16,B)-(c15,icosa,R)-(c14,B)-(c15,cosa,R)-(c15,B)-(c15,B,S)-(C02,B)-(C03,B,R)-(C03,B)-(C03,eta,S)-(c02,H)-(c03,H,R)-(c03,B)-(c04,icosa,R)-(c04,B)-(c04,B,S)-'
c1 = '(c02,H)-(c03,H,R)-(c12,H)-(c13,H,R)-(c22,H)-(c23,H,R)-(c32,H)-(c33,H,R)-(c42,H)-(c43,H,R)-(c52,H)-(c53,H,R)-(c62,H)-(c63,H,R)-(c72,H)-(c73,H,R)-(c82,H)-(c83,H,R)-(c92,H)-(c93,H,R)-'
c2 = '(c03,B)-(c04,icosa,R)-(c13,B)-(c16,hen,R)-(c23,B)-(c14,do,R)-(c33,B)-(c14,tri,R)-(c43,B)-(c14,tetra,R)-(c53,B)-(c14,penta,R)-(c63,B)-(c14,hexa,R)-(c73,B)-(c14,hepta,R)-(c83,B)-(c14,octa,R)-(c93,B)-(c14,nona,R)-'
 
d = '(e01,H)-(E02,H,R)-(d01,H)-(D02,H,R)-(d01,0)-(d02,0,R)-(d01,1)-(d12,1,R)-(d01,2)-(d22,2,R)-(d01,3)-(d32,3,R)-(d01,4)-(d42,4,R)-(d01,5)-(d52,5,R)-(d01,6)-(d62,6,R)-(d01,7)-(d72,7,R)-(d01,8)-(d82,8,R)-(d01,9)-(d92,9,R)-(D02,B)-(D03,B,R)-(D03,B)-(D03,propa,S)-(d14,B)-(d15,triacontano,R)-(d15,B)-(d15,B,S)-'
d1 = '(d02,H)-(d14,H,R)-(d12,H)-(d13,H,R)-(d22,H)-(d23,H,R)-(d32,H)-(d33,H,R)-(d42,H)-(d43,H,R)-(d52,H)-(d53,H,R)-(d62,H)-(d63,H,R)-(d72,H)-(d73,H,R)-(d82,H)-(d83,H,R)-(d92,H)-(d93,H,R)-'
d2 = '(d13,B)-(d14,hen,R)-(d23,B)-(d14,do,R)-(d33,B)-(d14,tri,R)-(d43,B)-(d14,tetra,R)-(d53,B)-(d14,penta,R)-(d63,B)-(d14,hexa,R)-(d73,B)-(d14,hepta,R)-(d83,B)-(d14,octa,R)-(d93,B)-(d14,nona,R)-' 

e = '(e01,H)-(E02,H,R)-(e01,H)-(E02,H,R)-(e01,0)-(e02,0,R)-(e01,1)-(e12,1,R)-(e01,2)-(e22,2,R)-(e01,3)-(e32,3,R)-(e01,4)-(e42,4,R)-(e01,5)-(e52,5,R)-(e01,6)-(e62,6,R)-(e01,7)-(e72,7,R)-(e01,8)-(e82,8,R)-(e01,9)-(e92,9,R)-(E02,B)-(E03,B,R)-(E03,B)-(E03,buta,S)-(e14,B)-(e15,tetraconta,R)-(e15,B)-(e15,B,S)-'
e1 = '(e02,H)-(e14,H,R)-(e12,H)-(e13,H,R)-(e22,H)-(e23,H,R)-(e32,H)-(e33,H,R)-(e42,H)-(e43,H,R)-(e52,H)-(e53,H,R)-(e62,H)-(e63,H,R)-(e72,H)-(e73,H,R)-(e82,H)-(e83,H,R)-(e92,H)-(e93,H,R)-'
e2 = '(e13,B)-(e14,hen,R)-(e23,B)-(e14,eo,R)-(e33,B)-(e14,tri,R)-(e43,B)-(e14,tetra,R)-(e53,B)-(e14,penta,R)-(e63,B)-(e14,hexa,R)-(e73,B)-(e14,hepta,R)-(e83,B)-(e14,octa,R)-(e93,B)-(e14,nona,R)-'

f = '(f01,H)-(F02,H,R)-(f01,H)-(F02,H,R)-(f01,0)-(f02,0,R)-(f01,1)-(f12,1,R)-(f01,2)-(f22,2,R)-(f01,3)-(f32,3,R)-(f01,4)-(f42,4,R)-(f01,5)-(f52,5,R)-(f01,6)-(f62,6,R)-(f01,7)-(f72,7,R)-(f01,8)-(f82,8,R)-(f01,9)-(f92,9,R)-(F02,B)-(F03,B,R)-(F03,B)-(F03,penta,S)-(f14,B)-(f15,pentaconta,R)-(f15,B)-(f15,B,S)-'
f1 = '(f02,H)-(f14,H,R)-(f12,H)-(f13,H,R)-(f22,H)-(f23,H,R)-(f32,H)-(f33,H,R)-(f42,H)-(f43,H,R)-(f52,H)-(f53,H,R)-(f62,H)-(f63,H,R)-(f72,H)-(f73,H,R)-(f82,H)-(f83,H,R)-(f92,H)-(f93,H,R)-'
f2 ='(f13,B)-(f14,hen,R)-(f23,B)-(f14,do,R)-(f33,B)-(f14,tri,R)-(f43,B)-(f14,tetra,R)-(f53,B)-(f14,penta,R)-(f63,B)-(f14,hexa,R)-(f73,B)-(f14,hepta,R)-(f83,B)-(f14,octa,R)-(f93,B)-(f14,nona,R)-'

g = '(g01,H)-(G02,H,R)-(g01,H)-(G02,H,R)-(g01,0)-(g02,0,R)-(g01,1)-(g12,1,R)-(g01,2)-(g22,2,R)-(g01,3)-(g32,3,R)-(g01,4)-(g42,4,R)-(g01,5)-(g52,5,R)-(g01,6)-(g62,6,R)-(g01,7)-(g72,7,R)-(g01,8)-(g82,8,R)-(g01,9)-(g92,9,R)-(G02,B)-(G03,B,R)-(G03,B)-(G03,hexa,S)-(g14,B)-(g15,hexaconta,R)-(g15,B)-(g15,B,S)-'
g1 = '(g02,H)-(g14,H,R)-(g12,H)-(g13,H,R)-(g22,H)-(g23,H,R)-(g32,H)-(g33,H,R)-(g42,H)-(g43,H,R)-(g52,H)-(g53,H,R)-(g62,H)-(g63,H,R)-(g72,H)-(g73,H,R)-(g82,H)-(g83,H,R)-(g92,H)-(g93,H,R)-'
g2 = '(g13,B)-(g14,hen,R)-(g23,B)-(g14,do,R)-(g33,B)-(g14,tri,R)-(g43,B)-(g14,tetra,R)-(g53,B)-(g14,penta,R)-(g63,B)-(g14,hexa,R)-(g73,B)-(g14,hepta,R)-(g83,B)-(g14,octa,R)-(g93,B)-(g14,nona,R)-'

h = '(h01,H)-(H02,H,R)-(h01,H)-(H02,H,R)-(h01,0)-(h02,0,R)-(h01,1)-(h12,1,R)-(h01,2)-(h22,2,R)-(h01,3)-(h32,3,R)-(h01,4)-(h42,4,R)-(h01,5)-(h52,5,R)-(h01,6)-(h62,6,R)-(h01,7)-(h72,7,R)-(h01,8)-(h82,8,R)-(h01,9)-(h92,9,R)-(H02,B)-(H03,B,R)-(H03,B)-(H03,hepta,S)-(h14,B)-(h15,heptaconta,R)-(h15,B)-(h15,B,S)-'
h1 = '(h02,H)-(h14,H,R)-(h12,H)-(h13,H,R)-(h22,H)-(h23,H,R)-(h32,H)-(h33,H,R)-(h42,H)-(h43,H,R)-(h52,H)-(h53,H,R)-(h62,H)-(h63,H,R)-(h72,H)-(h73,H,R)-(h82,H)-(h83,H,R)-(h92,H)-(h93,H,R)-'
h2 = '(h13,B)-(h14,hen,R)-(h23,B)-(h14,do,R)-(h33,B)-(h14,tri,R)-(h43,B)-(h14,tetra,R)-(h53,B)-(h14,penta,R)-(h63,B)-(h14,hexa,R)-(h73,B)-(h14,hepta,R)-(h83,B)-(h14,octa,R)-(h93,B)-(h14,nona,R)-'


i = '(i01,H)-(I02,H,R)-(i01,H)-(I02,H,R)-(i01,0)-(i02,0,R)-(i01,1)-(i12,1,R)-(i01,2)-(i22,2,R)-(i01,3)-(i32,3,R)-(i01,4)-(i42,4,R)-(i01,5)-(i52,5,R)-(i01,6)-(i62,6,R)-(i01,7)-(i72,7,R)-(i01,8)-(i82,8,R)-(i01,9)-(i92,9,R)-(I02,B)-(I03,B,R)-(I03,B)-(I03,octano,S)-(i14,B)-(i15,octaconta,R)-(i15,B)-(i15,B,S)-'
i1 = '(i02,H)-(i14,H,R)-(i12,H)-(i13,H,R)-(i22,H)-(i23,H,R)-(i32,H)-(i33,H,R)-(i42,H)-(i43,H,R)-(i52,H)-(i53,H,R)-(i62,H)-(i63,H,R)-(i72,H)-(i73,H,R)-(i82,H)-(i83,H,R)-(i92,H)-(i93,H,R)-'
i2 = '(i13,B)-(i14,hen,R)-(i23,B)-(i14,do,R)-(i33,B)-(i14,tri,R)-(i43,B)-(i14,tetra,R)-(i53,B)-(i14,penta,R)-(i63,B)-(i14,hexa,R)-(i73,B)-(i14,hepta,R)-(i83,B)-(i14,octa,R)-(i93,B)-(i14,nona,R)-'

j = '(j01,H)-(J02,H,R)-(j01,H)-(J02,H,R)-(j01,0)-(j02,0,R)-(j01,1)-(j12,1,R)-(j01,2)-(j22,2,R)-(j01,3)-(j32,3,R)-(j01,4)-(j42,4,R)-(j01,5)-(j52,5,R)-(j01,6)-(j62,6,R)-(j01,7)-(j72,7,R)-(j01,8)-(j82,8,R)-(j01,9)-(j92,9,R)-(J02,B)-(J03,B,R)-(J03,B)-(J03,nona,S)-(j14,B)-(j15,nonaconta,R)-(j15,B)-(j15,B,S)-'
j1 = '(j02,H)-(j14,H,R)-(j12,H)-(j13,H,R)-(j22,H)-(j23,H,R)-(j32,H)-(j33,H,R)-(j42,H)-(j43,H,R)-(j52,H)-(j53,H,R)-(j62,H)-(j63,H,R)-(j72,H)-(j73,H,R)-(j82,H)-(j83,H,R)-(j92,H)-(j93,H,R)-'
j2 = '(j13,B)-(j14,hen,R)-(j23,B)-(j14,do,R)-(j33,B)-(j14,tri,R)-(j43,B)-(j14,tetra,R)-(j53,B)-(j14,penta,R)-(j63,B)-(j14,hexa,R)-(j73,B)-(j14,hepta,R)-(j83,B)-(j14,octa,R)-(j93,B)-(j14,nona,R)-'

datos = datos+a+b+b1+b2+c+c1+c2+d+d1+d2+e+e1+e2+f+f1+f2+g+g1+g2+h+h1+h2+i+i1+i2+j+j1+j2 


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
    print('a')
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
                
                print('proximo valor a encontrar: ',cinta[contadorCinta])
                break
    print(cinta) 
    return cinta          
final = maquina('C51H30') 
respuestaFinal = ''
for i in final:
    
    if i != '1' and i != '2' and i != '3' and i != '4'and i != '5'and i != '6'and i != '7'and i != '8'and i != '9'and i != '0' and i != 'H' and i != 'B': 
       respuestaFinal = respuestaFinal + i
res =respuestaFinal + 'no'
print(res)

# nuevo = f2.replace('f','j').replace('F','J') 
# print(nuevo)