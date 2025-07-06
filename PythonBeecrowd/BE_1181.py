L = int(input())
T = str(input())

matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

matrizLinha = matriz[L]

soma = float(sum(matrizLinha))
if T == 'S':
    print(f'{soma:.1f}')
if T == 'M':
    media = soma / len(matrizLinha)
    print(f'{media:.1f}')