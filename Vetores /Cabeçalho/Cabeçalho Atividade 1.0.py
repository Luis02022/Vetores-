import os 

def media (n1, n2):
    resultado = n1 + n2
    mediar = resultado / 2
    return mediar

os.system("cls || clear")

prim_numero = int(input("Digite o primeiro número:"))
seg_numero = int(input("Digite o segundo número:"))

mediaTotal = media(prim_numero,seg_numero)

print(f"Média do aluno vale {mediaTotal}")