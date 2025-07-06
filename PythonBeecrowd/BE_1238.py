N = int(input())
resposta = ''
for _ in range(N):
    linha1, linha2 = map(str, input().split())

    tamanho = min(len(linha1), len(linha2))

    for i in range(tamanho):
        resposta = resposta + linha1[i] + linha2[i]
    
    if tamanho == len(linha2):
        resposta = resposta + linha1[tamanho:]
    else:
        resposta = resposta + linha2[tamanho:]
    
    print(resposta)
    resposta = ''