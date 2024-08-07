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


# print(f'X[1] = {X[1]}')
# print(f'X[2] = {X[2]}')
# print(f'X[3] = {X[3]}')
# print(f'X[4] = {X[4]}')
# print(f'X[5] = {X[5]}')
# print(f'X[6] = {X[6]}')
# print(f'X[7] = {X[7]}')
# print(f'X[8] = {X[8]}')
# print(f'X[9] = {X[9]}')
