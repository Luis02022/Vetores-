import os 
#Criando uma constante
QUANTIDADES_NOTAS = 3

os.system("cls || clear")
soma = 0
notas = []
media = 0
#contador = 0

for i in range (QUANTIDADES_NOTAS):
    nota = float(input(f"Digite sua {i+1}ª nota:"))
    notas.append(nota)
    #soma+=notas[i]
    #contador = contador + 1

os.system("cls || clear")

#ForEach
for nota in notas:
    print(f"Notas:{nota}")

media = sum(notas) / QUANTIDADES_NOTAS
#media = soma / QUANTIDADES_NOTAS
print(f"Média vale {media:.2}")
