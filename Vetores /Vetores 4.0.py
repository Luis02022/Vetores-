import os 
import sys 

numeros = []


QUANTIDADES_NUMEROS = 5
os.system("cls || clear")


while True:
  num = float(input("Digite um número:"))
  
  if num == 0:
    break
  numeros.append(num)     

  maior_num = max(numeros)
  menor_num = min(numeros)

for i, num in enumerate(numeros):
    print(f"{i+1}ª Nota: {num}")

#Exibindo números maiores e menores 
print(f"Maior número = {maior_num}")
print(f"Menor número = {menor_num}")
    