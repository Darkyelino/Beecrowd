N = int(input())
while N != 0:
    testes = list(map(int, input().split()))
    pilha = []

    for item in testes:
        if item in pilha:
            pilha.remove(item)
        else:
            pilha.append(item)
    print(pilha[0])
    N = int(input())