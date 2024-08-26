n = int(input())
i = 1
soma = 0
status = False
while i < n:
    print(i)
    soma = soma + i
    i = i + 1
    if i == 5:
        status = True
print(soma)
print(status)