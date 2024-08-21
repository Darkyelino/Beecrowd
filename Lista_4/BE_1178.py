X = float(input())
N = []

N.append(X)

for i in range(1, 100):
    metade = N[i-1] / 2
    N.append(metade)

for i in range(100):
    print(f'N[{i}] = {N[i]:.4f}')