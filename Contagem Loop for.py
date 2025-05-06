import time
import sys

#Barra de loading for funsies
total = 43
print("Carregando:")
for i in range(total + 1):
    barra = "=" * i + " " * (total - i)
    porcentagem = int((i / total ) * 100)
    print(f"\r[{barra}] {porcentagem}%", end = "", flush = True)
    time.sleep(0.08)

print("\nConcluído!\n")

#Contagem com "For"
print("==============Contagem com For==============")
print("Digite um número para a contagem")
x = int(input("Insira o número: "))
contagem = 0

for contagem in range(1, x + 1):
    print(contagem)
        
print("Contagem terminada!")
print("===========================================")

