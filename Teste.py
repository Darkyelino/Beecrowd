# BASICO TESTE
# print("Qual seu nome?")
# nome = str(input())
# print("Qual sua idade?")
# idade = int(input())
# print("Quanto é 1.0 + 0.5?")
# resposta = float(input())
#
# if (resposta == 1.5):
#     print(f'Seu nome é {nome} e sua idade é {idade}')
# else:
#     print('Você é burro meu parceiro')

# LISTAS
notas = [10.0, 9.5, 8.7, 9.1, 'erro', 'erro', 'erro']
notas.append(input())
print(f'Foi encontrado erro na lista: {notas}')
if int(notas[7]) <= 10:
    if notas[4] == 'erro':
        for i in range(len(notas)):
            if notas[i] == 'erro':
                del notas[i]
                print(notas)
    print(notas)

# elif int(notas[7]) > 10:
#     print('A nota inserida é maior que 10')
#     i = 0
#     for i in range(len(notas)):
#         del notas[i]
#     print(notas)

