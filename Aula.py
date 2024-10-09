# while True:
#     try:
#         N = int(input())
#         if N == 0:
#             print('vai ter copa!')
#         elif N != 0:
#             print('vai ter duas!')
#     except EOFError:
#         break

num = [1,2,3,4,5,6,7,8,9,10]

quadrados = [item*item for item in num]
print(quadrados)
print('\n')

pares = [i for i in num if i%2==0]
print(pares)
print('\n')

#Lista com pares e quadrados impares
lista = [i if i%2==0 else i*i for i in num]
print(lista)
print('\n')

letras = ['a','b','c','d','e']
#Lista que combina todas as letras com os números
combina = [(letra,n) for letra in letras for n in num]
print(combina)
print('\n')

combina2 = [(letra, n) for n in num for letra in letras]
print(combina2)
print('\n')

combina3 = [[letra, n] for n in num for letra in letras]
print(combina3)
print('\n')

matriz = [[j+1+i*4 for j in range(4)] for i in range(4)]
print(matriz)

# Jeito que eu sei fazer (nem isso)
transpostinha = []
for j in range(4):
    linha = []
    for i in range(3):
        linha.append(matriz[i][j])
    transpostinha.append(linha)
print(transpostinha)

# Jeito BASED REDPILL SIGMA DA BAHIA E EXTREME POGGERS MOLHADOR DE COCOTAS DE SER FEITO
transposta = [[matriz[i][j] for i in range(3)] for j in range(4)]
print(transposta)

#Usando Stringssssssssssssssss
frutas = [' abacate', ' banana ', 'abacaxi ']
novas_frutas = [fruta.strip().upper() for fruta in frutas]
print(novas_frutas)

frase = 'Exemplo de set comprehesion'
vogais_todas = [i for i in frase if i in 'aeiou']
vogais_unicas = [i for i in frase if i in 'Eaiou']
print(vogais_todas)
print(vogais_unicas)
vogais_dict = {i:i.upper() for i in frase if i in 'aeiou'}
print(vogais_dict)
