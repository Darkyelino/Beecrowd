X = []
i = 0

while i < 10:
    X.append(input())
    i = i + 1

for i in range(0, 10):
    if int(X[i]) <= 0:
        X[i] = 1

for i in range(0, 10):
    print(f'X[{i}] = {X[i]}')
