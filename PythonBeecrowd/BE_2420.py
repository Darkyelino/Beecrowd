N = int(input())
populacoes = list(map(int, input().split()))

soma_total = sum(populacoes)/2
diferenca = 0
fronteira = 0

for i in range(N):
    if diferenca != soma_total:
        fronteira = fronteira + 1
        diferenca = diferenca + populacoes[0]
        populacoes.pop(0)
print(fronteira)