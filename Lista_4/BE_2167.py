N = int(input())
lista = []
lista = input().split()
valor = 0

for i in range(1, N):
	if int(lista[i-1]) > int(lista[i]):
		valor = i + 1
		break

print(valor)