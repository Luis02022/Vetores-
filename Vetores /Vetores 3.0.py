import os 
import sys 

numeros = []
#maior_num = 0
#menor_num = 999999
QUANTIDADES_NUMEROS = 5
os.system("cls || clear")

for i in range (QUANTIDADES_NUMEROS):
    num = int(input(f"Digite o {i+1}ª número: \n"))
    numeros.append(num)    

maior_num = max(numeros)
menor_num = min(numeros)

for i, num in enumerate(numeros):
    #print(f"{i+1}ª Nota: {num}")

 print(f"Números {numeros[i]}")
#Exibindo números maiores e menores 
print(f"Maior número = {maior_num}")
print(f"Menor número = {menor_num}")
    