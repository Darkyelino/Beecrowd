N = int(input())
for _ in range(N):
    X = int(input())
    if X == 0:
        print("NULL")
    elif X % 2 == 0:
        if X > 0:
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    else:
        if X > 0:
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")