import os 

pares = 0
impares = 0

os.system("cls || clear")

def logoSenai():
    os.system("cls || clear")
    print("="*12)
    print("|||SENAI|||")
    print("="*12)

def par (num):
 for num in range numeros:  
    if num % 2 == 0:
     pares+=1
    return pares

def impar (num):
    if num % 2 != 0:
     impares+=1
    return impares

QUANT = 6
lista_de_numeros = []

for i in range (QUANT):
    logoSenai()
    numero = int(input("Digite um número:"))

    numpar = par(numero)   
    numimpar = impar(numero[i])

print(numpar)
print(numimpar)


