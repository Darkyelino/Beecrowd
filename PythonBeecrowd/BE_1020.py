dias_idade = int(input())

ano = dias_idade // 365
dias_restantes = dias_idade % 365
meses = dias_restantes // 30
dias = dias_restantes % 30

print(f'{ano} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')