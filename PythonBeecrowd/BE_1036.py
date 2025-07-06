A, B, C = map(float, input().split())
A = float(A)
B = float(B)
C = float(C)
delta = float(B**2 - 4*A*C)

if A == 0:
    print("Impossivel calcular")
elif delta < 0:
    print("Impossivel calcular")
else:
    R1 = float((-B + delta**0.5) / (2 * A))
    R2 = float((-B - delta**0.5) / (2 * A))
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")