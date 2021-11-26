#estados iniciales
# letra = 'abcdefghijk'
# valores = '012345678910'
# contador = 0
# impresion = ''
# final = ''
# for i in range(10):
#     #impresion = impresion + '('+letra[i]+'00,'+valores[i]+')-('+letra[i]+'0'+str(contador)+',',valores[i]+',R),'
#     impresion = '(j01,'+valores[i]+')-(j'+str(contador)+'2,'+valores[i]+',R)-'
#     print('(j01,',valores[i],')-(j',str(contador),'2,',valores[i],',R)-')
#     if(i == 10):
#         #impresion = impresion + '('+letra[i]+'00,'+valores[i]+')-('+letra[i]+'0'+str(contador)+',',valores[i]+'0,R),'
#         impresion = '(j01,'+valores[i]+')-(j'+str(contador)+'2,'+valores[i]+',R)-'
#         print('(j01,',valores[i],')-(j',str(contador),'2,',valores[i],',R)-')
#     final = final + impresion
  
#     contador += 1
# impresion.replace(' ','')
# print(final)       



#segunda linea de estados
# letra = 'abcdefghijk'
# valores = '123456789'
# prefijos = ['un','do','tri','tetra','penta','hexa','hepta','octa','nona']
# contador = 1
# impresion = ''
# finalImpresionSegunda = ''   
# for i in range(9):

#     print('(b',valores[i],'3,B)-(b14,',prefijos[i],',R)-')
#     impresion = '(b'+valores[i]+'3,B)-(b14,'+prefijos[i]+',R)-'
#     finalImpresionSegunda = finalImpresionSegunda +impresion
  
#     contador += 1
# impresion.replace(' ','')
# print(finalImpresionSegunda)

#primera linea
letra = 'abcdefghijk'
valores = '123456789'
prefijos = ['un','do','tri','tetra','penta','hexa','hepta','octa','nona']
contador = 1
impresion = ''
finalImpresionSegunda = ''   
for i in range(9):

    print('(b',valores[i],'2,H)-(b',valores[i],'3,H,R)-')
    impresion = '(b'+valores[i]+'2,H)-(b'+valores[i]+'3,H,R)-'
    finalImpresionSegunda = finalImpresionSegunda +impresion
  
    contador += 1
impresion.replace(' ','')
print(finalImpresionSegunda)

