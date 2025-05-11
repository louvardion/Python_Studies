import numpy as np
import bisect

#criando listas 

lista = [1, 2, 5, None]
tup = ('abc', 'def', 'ghi')
lista1 = list(tup)
lista2 = [None]*5

print(lista)
print(lista1)
print(lista2)

#indexando/adicionando/concatenand/somando listas

lista.append(lista2)
lista1.insert(1,"123")

print(lista)
print(lista1)
print(lista2)
print(2 in lista)
print(2 not in lista)

lista3 = [10, 20, 30, 40, 50] + lista1
lista4 = [9, 8, 7, 6, 5] 

print(lista3)
print(lista4)

#Extendendo listas

lista4.extend(['Ooh', 'Girl', 'She', 'Done', 'Already', 'Done','Had', 'Herse.'])

print(lista4)

lista5 = [3, 7, 0, 9, 25, 10]

print(lista5)

#sort()

lista5.sort()

print(lista5)

bisect.bisect(lista5, 8)
bisect.insort(lista5, 8)

print(lista5)

#Lista[inicio:parada:passo] - Usando Slice!

lista6 = [9, 2, 0, 1, 3, 2, 6, 8]
lista6.sort(reverse=True)

print(lista6)
print(lista6[0:6:2])
print(lista6[::-1])
print(lista6[7:1:-2])

#enumerate(list)

for i, value in enumerate(lista6):
    print(value, ':', i)

#sorted()

lista7 = [4,2,5,3,1]
string = 'teste'

print(lista7)
print(sorted(lista7))
print(string)
print(sorted(string))

#zip

lista8 = ['amor', 'bahia', 'casa']
lista9 = [1, 2, 3]
lista10 = ['amizade', 'pernambuco']
lista_zipada = zip(lista8, lista9, lista10)

print(list(lista_zipada))

p = [True, False, False, True]
q = [True, True, True, False]
PorQ = []

for (a,b) in zip(p,q):
    PorQ.append(a or b)
    
print(PorQ)

#unzip

participantes = [('Anne', 'Hathaway'),('Lupita', 'Nyongo'), ('Natalie', 'Portman')]
nome, sobrenome = zip(*participantes)

print(participantes)
print(sobrenome)
print(nome)

#list comprehensions
#Montando um if muito feio no meio de um for:
#nomes = ['Alberto', 'Amanda', 'Genoveva', 'Jaislaine','Septembro', 'Joanele', 'Anita', 'Lurdes']
#resultado = []

#for x in nomes:
#        if x[0].lower() == 'a':
#             resultado.append(x.upper())
#Ao invés disso, fazer:

nomes = ['Alberto', 'Amanda', 'Genoveva', 'Jaislaine','Septembro', 'Joanele', 'Anita', 'Lurdes']
resultado = [x.upper() for x in nomes if x[0].lower() == 'a']

print(resultado)

#experimentando zip em outras coisas

nomes1 = ['Catarina', 'Júlio', 'César']
sobrenomes1 = ['Silva', 'Costa', 'Lippaus']
idades1 = [23, 22, 23]
pesos1 = [60.1, 70.5, 88.6]
clientes1 = zip(nomes1, sobrenomes1, idades1, pesos1)

print(list(clientes1))
