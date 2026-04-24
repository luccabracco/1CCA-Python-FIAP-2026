qtd_music = int(input("Digite a quantidade de musica que voce tem na sua playlist: "))

for i in range(qtd_music):
    print(f"Musica {i}")

# repeticoes encadeadas

for l in range(0, 4):
    for j in range(0, 3, 2):
        print(f"l = {l}, j = {j}")