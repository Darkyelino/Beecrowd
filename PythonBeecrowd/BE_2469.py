N = int(input())
X = list(map(int, input().split()))
maior = 0
repetido = 0

for i in range(N):
    contador = 0
    for j in range(N):
        if int(X[i]) == int(X[j]):
            contador = contador + 1
        if contador > maior or (contador == maior and int(X[i]) > repetido):
            maior = contador
            repetido = int(X[i])
print(repetido)
