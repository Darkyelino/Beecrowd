N = int(input())
for i in range(N):
    led = 0
    linha = list(map(int, input()))
    for i in linha:
        if i == 1:
            led += 2
        elif i == 2:
            led += 5
        elif i == 3:
            led += 5
        elif i == 4:
            led += 4
        elif i == 5:
            led += 5
        elif i == 6:
            led += 6
        elif i == 7:
            led += 3
        elif i == 8:
            led += 7
        elif i == 9:
            led += 6
        elif i == 0:
            led += 6
    print(f'{led} leds')