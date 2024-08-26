alcool = 0
gasolina = 0
diesel = 0

while True:
    n = int(input())

    if n == 4:
        break
    elif n == 1:
        alcool = alcool + 1
    elif n == 2:
        gasolina = gasolina + 1
    elif n == 3:
        diesel = diesel + 1
    
print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")



