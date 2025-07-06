N1, N2, N3, N4 = map(float, input().split())
peso1, peso2, peso3, peso4 = 2, 3, 4, 1

media = (N1 * peso1 + N2 * peso2 + N3 * peso3 + N4 * peso4) / (peso1 + peso2 + peso3 + peso4)

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    media_final = (media + exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")