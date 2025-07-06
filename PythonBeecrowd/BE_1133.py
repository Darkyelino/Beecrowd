A = int(input())
B = int(input())
if B < A:
    aux = A
    A = B
    B = aux
for i in range(A+1, B):
    if i%5==2 or i%5==3:
        print(i)