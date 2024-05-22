import os 

os.system("cls || clear")
soma = 0
notas = []
media = 0
contador = 0

for i in range (3):
    nota = float(input(f"Digite sua {i+1}ª nota:"))
    notas.append(nota)
    soma+=notas[i]
    contador = contador + 1

os.system("cls || clear")
for i in range (3):
    print(f"{i+1}ª notas = {notas[i]}")

media = soma / contador
print(f"Média vale {media}")
