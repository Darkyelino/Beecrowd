N = int(input())
ant = 0; prox = 1
if N < 2:
    print(ant)
else:
    print(ant, prox, end=' ')
    for i in range(1,N-2):
        aux = ant
        ant = prox
        prox = aux + ant
        print(prox, end=' ')
    print(aux+ant)