A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

if A > B and A > C:
	maior = A
elif B > A and B > C:
	maior = B
elif C > A and C > B:
	maior = C

if A < B and A < C:
	menor = A
elif B < A and B < C:
	menor = B
elif C < A and C < B:
	menor = C

if A != maior and A != menor:
	meio = A
elif B != maior and B != menor:
	meio = B
elif C != maior and C != menor:
	meio = C
	
print(f'{menor}')
print(f'{meio}')
print(f'{maior}')
print()
print(f'{A}')
print(f'{B}')
print(f'{C}')