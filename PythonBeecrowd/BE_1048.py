salario = float(input())

if salario <= 400.00:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    percentual = 15
elif salario <= 800.00:
    aumento = salario * 0.12
    novo_salario = salario + aumento
    percentual = 12
elif salario <= 1200.00:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    percentual = 10
elif salario <= 2000.00:
    aumento = salario * 0.07
    novo_salario = salario + aumento
    percentual = 7
else:
    aumento = salario * 0.04
    novo_salario = salario + aumento
    percentual = 4

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {aumento:.2f}")
print(f"Em percentual: {percentual} %")