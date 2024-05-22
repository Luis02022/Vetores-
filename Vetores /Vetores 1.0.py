import os 

os.system("cls || clear")
#Criando uma lista / vetor 
notas = []

#Solicitando 3 notas para o usuário
for i in range (3):
    nota = float(input("Digite sua nota:"))
    notas.append(nota)#Append irá colocar o valor de outra variável

os.system("cls || clear")
#Exibindo dados 
for i in range (3):
    print(f"{i+1}ª Nota: {notas[i]}")