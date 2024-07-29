N = int(input())

print(N)

print(f"{N//100} nota(s) de R$ 100,00")
Novo_N = N%100
print(f"{Novo_N//50} nota(s) de R$ 50,00")
Novo_N = Novo_N%50
print(f"{Novo_N//20} nota(s) de R$ 20,00")
Novo_N = Novo_N%20
print(f"{Novo_N//10} nota(s) de R$ 10,00")
Novo_N = Novo_N%10
print(f"{Novo_N//5} nota(s) de R$ 5,00")
Novo_N = Novo_N%5
print(f"{Novo_N//2} nota(s) de R$ 2,00")
Novo_N = Novo_N%2
print(f"{Novo_N} nota(s) de R$ 1,00")