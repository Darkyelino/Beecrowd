N = int(input().strip())

for _ in range(N):
    quantidade, numero = map(int, input().split())
    palpites = list(map(int, input().split()))

    melhor_palpite = 0
    menor_diferenca = abs(numero - palpites[0])

    for i in range(1, quantidade):
        diferenca = abs(numero - palpites[i])
        if diferenca < menor_diferenca:
            melhor_palpite = i
            menor_diferenca = diferenca
    
    print(melhor_palpite + 1)
