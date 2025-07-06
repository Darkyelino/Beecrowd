N = int(input())
sobra_segundos = N % 3600
horas = N // 3600
minutos = sobra_segundos // 60
segundos = sobra_segundos % 60
print(f'{horas}:{minutos}:{segundos}')