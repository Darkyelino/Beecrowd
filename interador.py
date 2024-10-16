# Criar um iterador:
interador = iter('123456789')
# print(next(iterador), next(iterador), next(iterador), next(iterador), next(iterador), next(iterador), next(iterador), next(iterador), next(iterador))

# Qualquer iteravel pode ser percorrido com laço:
for i in interador:
    print(i)

# Percorre o iterator, se eu não comentar, não printa o dicionario.
alunos = ['Alice', 'Bernardo', 'Carlos']
alunos_interador = enumerate(alunos)
# for t  in alunos_iterator:
#     print(t)

# Retorna um iterador:
reverso = reversed(alunos)
print(type(reverso))
for i in reverso:
    print(i)

# Cria dicionario a partir de iterador:
# Como foi percorrido no 'for' de alunos_iterator, se eu não comentar, não printa o dicionario.
dicionario = dict(alunos_interador)
print(dicionario)

numeros = [10,20,30,40,50]
quadrados = (n**2 for n in numeros)
combinacao = zip(numeros, quadrados) #Sempre percorrera até o tamanho da menor coleção

for i in combinacao:
    print(i)