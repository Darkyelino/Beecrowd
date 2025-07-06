A, B, C = map(float, input().split())
if A < B:
    A, B = B, A
if A < C:
    A, C = C, A
if B < C:
    B, C = C, B

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == (B**2 + C**2):
        print("TRIANGULO RETANGULO")
    if A**2 > (B**2 + C**2):
        print("TRIANGULO OBTUSANGULO")
    if A**2 < (B**2 + C**2):
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    if (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
        print("TRIANGULO ISOSCELES")