nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")
nome4 = input("Digite o quarto nome: ")

nomes = (nome1, nome2, nome3, nome4)

print()
print("Possiveis Duplas:")
print()

for i in range(len(nomes)):
    for j in range(i + 1, len(nomes)):
        print(f"{nomes[i]} e {nomes[j]}")

# len = quantidade de variaveis