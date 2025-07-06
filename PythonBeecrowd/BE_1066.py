a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
par = 0
impar = 0
negativo = 0
positivo = 0

if (a % 2) == 0:
	par = par + 1
if (b % 2) == 0:
	par = par + 1
if (c % 2) == 0:
	par = par + 1
if (d % 2) == 0:
	par = par + 1
if (e % 2) == 0:
	par = par + 1	
if (a % 2) == 1:
	impar = impar + 1
if (b % 2) == 1:
	impar = par + 1
if (c % 2) == 1:
	impar = impar + 1
if (d % 2) == 1:
	impar = impar + 1
if (e % 2) == 1:
	impar = impar + 1
	
if a > 0:
	positivo = positivo + 1
if a < 0:
	negativo = negativo + 1
if b > 0:
	positivo = positivo + 1
if b < 0:
	negativo = negativo + 1
if c > 0:
	positivo = positivo + 1
if c < 0:
	negativo = negativo + 1
if d > 0:
	positivo = positivo + 1
if d < 0:
	negativo = negativo + 1
if e > 0:
	positivo = positivo + 1
if e < 0:
	negativo = negativo + 1

print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')