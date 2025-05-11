from collections import defaultdict
#Criando e alterando valores em dicionários

dicio = dict(ChaveA = 'ValorA', ChaveB = 'ValorB', ChaveN = 'ValorN')

print(dicio)
print(dicio['ChaveB'])

dicio['ChaveC'] = 'ValorC'

print(dicio)

dicio['ChaveN'] = 'Jake! Por favor!!!'

print(dicio)

#Localizando elementos

print('ChaveN' in dicio)
print('ValorA' in dicio)  #'in' Só busca chaves

#Deletando elementos

del dicio['ChaveN']

print(dicio)

dicio.pop('ChaveA')

print(dicio)

print(list(dicio.keys()))
print(list(dicio.values()))

#Combinando dicionarios

dici1 = {'Diego' : 962055038, 'Eduardo' : 996563220}
dici2 = {'Catléia' : 991900303, ' Eduardo' : 993322312}

dici1.update(dici2) #Ele mantém os dados do dicionario mais recente.

print(dici1)

#Transformar Lista em dicionario dicionario.setdefault().append()

nomes = ['Anderson', 'Helen', 'Andressa', 'Liana']
dici3 = {}

for x in nomes:
    letras = len(x)
    dici3.setdefault(letras, []).append(x)

print(dici3)

#Outra forma 

nomes1 = ['Anderson', 'Helen', 'Andressa', 'Liana']
dici4 = defaultdict(list)

for x in nomes1:
    dici4[len(x)].append(x)

dict(dici4)

print(dici4)

#Dict comprehensions: {chave:valor for valor in sequência if condição}

nomes2 = ['Anderson', 'Helen', 'Andressa', 'Liana', 'Alberto', 'Amanda', 'Genoveva', 'Jaislaine','Septembro', 'Joanele', 'Anita', 'Lurdes']

dici5 = {i : n for i, n in enumerate(nomes2) if len(n) < 6}

print(dici5)