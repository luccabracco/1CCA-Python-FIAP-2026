def validar_nota(nota):
    while nota < 0 or nota > 10:
        print("Nota invalida")
        nota = float(input("Digite a Nota novamente: "))
    return nota

nota_a = float(input("Digite a Primeira Nota: "))
nota_a = validar_nota(nota_a)

nota_b = float(input("Digite a Segunda Nota: "))
nota_b = validar_nota(nota_b)

media = (nota_a + nota_b) / 2
print(f"Sua media é de: {media:.2f}")