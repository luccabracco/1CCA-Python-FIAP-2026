musicas = [
    ["Chicago", "Michael Jackson"],
    ["Sorry", "Justin Bieber"],
    ["Judas", "Lady Gaga"]
]

# print(musicas[1][0])

for musica in musicas:
    for info in musica:
        print(info)
    print()

# Para ficar com o cantor do lado da musica usar - print(f"{musica[1]} - {musica[1]}")

for musica in musicas:
    print(f"{musica[0]} e {musica[1]}")