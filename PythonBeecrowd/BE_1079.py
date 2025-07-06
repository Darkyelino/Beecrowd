N = int(input())
for _ in range(N):
    A, B, C = map(float, input().split())
    media_ponderada = (A * 2 + B * 3 + C * 5) / 10
    print(f"{media_ponderada:.1f}")