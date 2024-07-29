Nota = float(input())

print('NOTAS:')
print(f"{Nota//100:.0f} nota(s) de R$ 100.00")
Nota = Nota%100
print(f"{Nota//50:.0f} nota(s) de R$ 50.00")
Nota = Nota%50
print(f"{Nota//20:.0f} nota(s) de R$ 20.00")
Nota = Nota%20
print(f"{Nota//10:.0f} nota(s) de R$ 10.00")
Nota = Nota%10
print(f"{Nota//5:.0f} nota(s) de R$ 5.00")
Nota = Nota%5
print(f"{Nota//2:.0f} nota(s) de R$ 2.00")
Nota = Nota%2

Moedas = int(Nota * 100)

print('MOEDAS:')
print(f"{Moedas//100:.0f} moeda(s) de R$ 1.00")
Moedas = Moedas%100
print(f"{Moedas//50:.0f} moeda(s) de R$ 0.50")
Moedas = Moedas%50
print(f"{Moedas//25:.0f} moeda(s) de R$ 0.25")
Moedas = Moedas%25
print(f"{Moedas//10:.0f} moeda(s) de R$ 0.10")
Moedas = Moedas%10
print(f"{Moedas//5:.0f} moeda(s) de R$ 0.05")
Moedas = Moedas%5
print(f"{Moedas//1:.0f} moeda(s) de R$ 0.01")
Moedas = Moedas%1