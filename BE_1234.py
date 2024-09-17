while True:
    try:
        setenca = str(input())
        continua = 2
        nova_frase = ""
        for letra in setenca:
            if letra == " ":
                nova_frase += " "
            else:
                if continua%2 == 0:
                    continua += 1
                    nova_frase += letra.upper()
                else:
                    continua += 1
                    nova_frase += letra.lower()
        print(nova_frase)
    except EOFError:
        break