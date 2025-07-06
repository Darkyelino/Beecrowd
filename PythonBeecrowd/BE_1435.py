valores = [4,5,6,7,12,11,13,1,2,3]

partidas = int(input())

partidaAdalberto = 0
partidaBernardete = 0

for i in range(partidas):
    cartas = list(map(int, input().split()))
    
    rodadasAdalberto = 0
    rodadasBernardete = 0
    
    for j in range(3):
        x = valores.index(int(cartas[j]))
        y = valores.index(int(cartas[j+3]))
        if x >= y:
            rodadasAdalberto += 1
        else:
            rodadasBernardete += 1
    if rodadasAdalberto > rodadasBernardete:
        partidaAdalberto += 1
    else:
        partidaBernardete += 1

print(partidaAdalberto, partidaBernardete)