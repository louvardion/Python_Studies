print("Digite um número para a contagem")
x = int(input("Insira o número: "))
contagem = 0

for contagem in range(x):
    if contagem < x:
        contagem += 1
        print(contagem)
    elif contagem == x:
        break