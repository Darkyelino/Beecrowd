N = int(input())
X = []
X = input().split()

menor = int(X[0])
posicao = 0

for i in range(1, N):
    if int(X[i]) < menor:
        menor = int(X[i])
        posicao = i

print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')