import sys
import time
import os

#Sim, ela voltou! A barra de carregamento!

barrinha_giratoria = ["\\","||", "//", "=="]
print("Carregando...", end = " ", flush = True)

for i in range (10):
    time.sleep(0.1)
    for frame in barrinha_giratoria:
        print(f"\rCarregando... {frame}", end = "", flush = True)
        time.sleep(0.1)

time.sleep(0.2)
os.system('cls' if os.name == 'nt' else 'clear')
print("\nConcluído!\n")

#Contagem com o While

print("=============Contagem com While=============")

contagem = 0

while True:
    entrada = input("Insira um número para a contagem: ")
    try:
        num = int(entrada)
        break
    except ValueError:
        print("Isso não é um número válido. Tente de novo.")


while contagem < num:
    contagem += 1
    print(contagem)


print("Contagem terminada!")
print("===========================================")