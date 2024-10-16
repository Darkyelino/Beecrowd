valor = [0, 1, 2, 4, 5]
somado = (v+2 for v in valor)
combinacao = zip(valor, somado)

for i in combinacao:
    print(i)