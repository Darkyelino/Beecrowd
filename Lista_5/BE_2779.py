N = int(input()) # Quantas Figurinhas totais tem o ALBUM
M = int(input()) # Quantas Figurinhas foi COLECIONADA

figurinhas = []
organizado = []
# Adicionando a lista de figurinhas colecionadas
for i in range(0, M):
    figurinhas.append(int(input()))
# Retirando as duplicatas para organizar
for elemento in figurinhas:
    if elemento not in organizado:
        organizado.append(elemento)

quantidade = len(organizado)
restante = int(N - quantidade)

print(restante)
    