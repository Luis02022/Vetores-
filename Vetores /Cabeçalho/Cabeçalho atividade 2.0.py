import os 

os.system("cls || clear")

def tabuada (n1):
    for i in range (1,11):
        print(f"{n1} x {i} = {n1 * i}")

numero = int(input("Digite um número para a tabuada:"))

tab = tabuada(numero)

print(tab)