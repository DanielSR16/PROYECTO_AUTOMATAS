import re

expresion ='[C](H4|2H6|3H8|4H10|5H12)'
p = re.compile('[C]([1-9]|[0-9]{2,3})[H]([1-9]{,2}[02468]|[1-9][02468]{,2})')

valor = p.fullmatch('C999H968')

print(valor)   