N = int(input())
i = 0
dentro = 0
fora = 0

while i < N:
	num = int(input())
	if 10 <= num <= 20:
		dentro = dentro + 1
	else:
		fora = fora + 1
	i = i + 1
	
print(f'{dentro} in')
print(f'{fora} out')