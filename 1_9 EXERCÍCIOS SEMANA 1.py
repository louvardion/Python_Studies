'''Área do triângulo

print('Insira os dados do triangulo a ser calculado:')
      
b = float(input('Insira valor da base: '))
h = float(input('Insira valor da altura: '))
      
aTriangulo = (b*h)/2
      
print('A area do triângulo é: ', aTriangulo)


#------------------------------------------------


print('Transformando segundos em horas e minutos.')

segs = int(input('Quantos segundos? '))

mins = int(segs / 60)

hors = int((segs/60)/60)

print(segs, ' segundos equivalem a ', mins, ' minutos e ', hors, ' horas.')
3

#-------------------------------------------------

print('Transformando horas em minutos e segundos.')

hors = int(input('Quantas horas? '))

mins = int(hors*60)

segs = int((hors*60)*60)

print(hors, ' horas equivalem a ', mins, ' minutos e ', segs, ' segundos.')

#-------------------------------------------------
'''

print('Cáculo de juros simples.')

C = float(input('Insira o capital: '))
I = float(input('Insira a taxa: '))
T = float(input('Insira o tempo: '))

J = float(C * I * T)/100

print('O juro composto resultou em: ', J)

