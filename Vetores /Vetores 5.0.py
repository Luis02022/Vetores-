import os 

QUANT = 6
pares = 0
impares = 0
numeros = []

os.system("cls || clear")

for i in range(QUANT):
    numero = int(input("Digite um número:"))
    numeros.append(numero)

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

for i,numero in enumerate(numeros):
    print(f"{i+1}ª Nota: {numero}")

print(f"Quantos pares digitado = {pares}")
print(f"Quantos impares digitado = {impares}")