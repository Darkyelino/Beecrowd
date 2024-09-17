while True:
    try:
        M, N = map(int, input().split())
        if M == 0 and N == 0:
            break
        else:
            soma =  str(M + N)
            resultado = ''
            for num in soma:
                if num == '0':
                    pass
                else:
                    resultado += num
            print(resultado)
    except EOFError:
        break