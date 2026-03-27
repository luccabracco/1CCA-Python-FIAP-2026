# Exercicios da Ultima aula de Python

# Exercicio 1
raio = 5
area = 3.14159 * (raio**2)

print(f"Exercicio 1 - A area é de: {area:.2f}")

# Exercicio 2 e 3
fahren = 98
celcius = (fahren - 32) * 5/9

print(f"Exercicio 2 e 3 - A temperatura em Celcius é: {celcius:.1f} graus")

# Exercicio 4
livros = 3 * 25
caneta = 2 * 5
total = livros + caneta

print(f"Exercicio 4 - O gasto total foi de: R${total},00")

# Exercicio 5
distancia = 150
velocidade = 60
tempo = distancia / velocidade

print(f"Exercicio 5 - O tempo que levou foi de: {tempo:.1f} Horas")

# Exercicio 6
a = 8
b = 9
media = (a + b) / 2

print(f"Exercicio 6 - A média do aluno foi: {media:.1f}")

# Exercicio 7
a2 = 2
b2 = 2
pesoa = 4
pesob = 6
media2 = (a2 * pesoa) + (b2 * pesob) / (pesoa + pesob)

print(f"Exercicio 7 - A media do aluno foi: {media2:.1f}")

# Exercicio 8
peça1 = 8
qnt_peça1 = 20
peça2 = 10
qnt_peça2 = 13
valor = (peça1 * qnt_peça1) + (peça2 * qnt_peça2)

print(f"Exercicio 8 - O valor a ser pago é de: R${valor:.2f}")

# Exercicio 9

produto = int(input("Digite o valor do produto: "))
pago = int(input("Digite o valor pago: "))
troco = pago - produto

print(f"Exercicio 9 - O troco é de: R${troco:.2f}")