num = int(input())
nova_linha = ''
contador = 1
for i in range(num):
    linha = str(input())
    for letra in linha:
        if contador == 1:
            nova_linha += letra
            contador = 0
        if letra == ' ':
            contador = 1
    print(nova_linha)