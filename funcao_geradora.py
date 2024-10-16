def imprimir():
    print('Imprime 1')
    yield 1
    print('Imprime 2')
    yield 2
    print('Imprime 3')
    yield 3

it = imprimir() # Retorno da função geradora é um interador
print(next(it), next(it))