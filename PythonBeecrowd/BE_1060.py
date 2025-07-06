n = 0
contador = 0
while n != 6:
    numero = int(input())
    n = n + 1
    if numero >= 0: 
        contador = contador + 1

print(f"{contador} valores positivos")