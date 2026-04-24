# CP = Contador de Produto

cp = 0
while cp < 3:
    print(f"Produto {cp}")
    cp += 1

# White drecescente de 4 até 1 (incluindo)

i = 4
while i > 0:
    print(i)
    i -= 1

# Repetindo com entrada do usuario

jogar = ("sim")

while jogar.lower() == "sim":
    print("Inicia ou repete o jogo")
    jogar = input("Deseja jogar novamente?(sim/nao) ")

# Modificadores de fluxo

i = 0
while i < 10:
    i += 1

    if i == 3 or i == 5:
        continue

    if i == 7:
        break

    print(f"Produto {i}")
