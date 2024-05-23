import os 

os.system("cls || clear")
def somar(n1,n2):
    resultado = n1 + n2
    return resultado 

def sub(n1,n2):
    resultado = n1 - n2
    return resultado

def mul(n1,n2):
    resultado = n1 * n2
    return resultado

def div(n1,n2):
    return n1/n2

#Solicitando dados 
primeiro_numero = int(input("Digite o primeiro número:"))
segundo_numero = int(input("Digite o segundo número:"))

soma = somar(primeiro_numero, segundo_numero)
subtracao = sub (primeiro_numero,segundo_numero)
multiplicacao = mul (primeiro_numero,segundo_numero)
divisão = div(primeiro_numero,segundo_numero)

os.system("cls || clear")

print(f"Soma = {soma}")  
print(f"Subtração = {subtracao}")  
print(f"Multiplicação = {multiplicacao}")  
print(f"Divisão = {divisão}")  
