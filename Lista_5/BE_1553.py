assassinos = [] #Lista pra guardar os N assassinos
# Repetição para capturar os N suspeitos
while True:
    N = int(input()) #Quantos suspeitos vão vir a seguir, se for 0 acaba
    if N == 0:
        break

    suspeitos = list(map(int, input().split())) #Lista de suspeitos

    suspeitosOrganizado = sorted(suspeitos) #Organiza a lista do menor para o maior
    suspeitosOrganizado.reverse() #Inverte as posições, ficando do maior para o menor
    segundoMaior = suspeitosOrganizado[1] #Variavel segundo maior recebe o segundo maior valor

    posicao = suspeitos.index(segundoMaior)+1 #Para capturar a posição da variavel segundo maior na lista de suspeitos

    assassinos.append(posicao) #Adiciona a posição do segundo maior suspeito na lista de asssassinos

for i in range(len(assassinos)):
    print(assassinos[i]) #Imprime cada um dos culpados por vez :D
