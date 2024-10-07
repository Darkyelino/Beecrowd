from functools import reduce

Fatura = [('Net', 199.9),('Ifood', 999.87),('Gasolina', 678.0),('Formigão', 400)]

# Reformatando
print(list(map(lambda x: f'Tipo de Gasto: {x[0]} - {x[1]}R$', Fatura)))

# Ordenando por valor
Fatura.sort(key = lambda x: x[1])
print(f'Ordenando os itens por valor: {Fatura}')

# Ordenado acima de quinhentos
print('Ordenado acima de quinhentos:')
print(list(filter(lambda x: x[1]>500, Fatura)))

# Total da fatura (jeitinho abel)
gastos = []
for chave, valor in Fatura:
    gastos.append(valor)

print('Total da Fatura:')
print(sum(gastos))

#Total da fatura (jeitinho mais certo)
total = list(map(lambda x: x[1], Fatura))
print(sum(total))

#Total da fatura (como professor fez)
# Não anotei xD
