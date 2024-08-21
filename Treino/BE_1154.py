x = 0
idade = 0
contador = 0
while True:
    x = int(input())
    if x > 0:
        idade = idade + x
        contador = contador + 1
    if x < 0:
        break
media = float(idade/contador)
print(f"{media:.2f}")