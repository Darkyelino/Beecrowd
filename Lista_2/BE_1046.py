inicio, fim = map(int, input().split())
duracao = 0
inicio = int(inicio)
fim = int(fim)

if inicio < fim:
    duracao = fim - inicio
elif inicio > fim:
    duracao = (24 - inicio) + fim
elif inicio == fim:
    duracao = 24

print(f"O JOGO DUROU {duracao} HORA(S)")