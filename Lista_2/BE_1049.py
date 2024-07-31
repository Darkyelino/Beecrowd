nivel1 = input().strip()
nivel2 = input().strip()
nivel3 = input().strip()

if nivel1 == "vertebrado":
    if nivel2 == "ave":
        if nivel3 == "carnivoro":
            print("aguia")
        elif nivel3 == "onivoro":
            print("pomba")
    elif nivel2 == "mamifero":
        if nivel3 == "onivoro":
            print("homem")
        elif nivel3 == "herbivoro":
            print("vaca")
elif nivel1 == "invertebrado":
    if nivel2 == "inseto":
        if nivel3 == "hematofago":
            print("pulga")
        elif nivel3 == "herbivoro":
            print("lagarta")
    elif nivel2 == "anelideo":
        if nivel3 == "hematofago":
            print("sanguessuga")
        elif nivel3 == "onivoro":
            print("minhoca")