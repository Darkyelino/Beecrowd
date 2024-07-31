A, B = input().split()
A = int(A)
B = int(B)

if A == 1:
	total = float(4.00)
elif A == 2:
	total = float(4.50)
elif A == 3:
	total = float(5.00)
elif A == 4:
	total = float(2.00)
elif A == 5:
	total = float(1.50)
	
total = float(total * B)
print(f'Total: R$ {total:.2f}')