P1, C1, P2, C2 = map(int, input().split())

esquerdo = P1 * C1
direito = P2 * C2

if (direito > esquerdo):
  print(1)
elif (esquerdo > direito):
  print(-1)
else:
  print (0)