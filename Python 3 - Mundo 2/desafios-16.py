"""
num0a20 = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove",
           "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete",
           "Dezoito", "Dezenove", "Vinte")
num = int(input("Digite um número entre 0 a 20: "))
while 0 > num or num > 20:
    num = int(input("\nPor favor, digite um número que entre 0 a 20: "))
print(num0a20[num])
"""

"""
classificacao = ("Palmeiras", "Corinthians", "Fluminense", "Athletico-PR",
                 "Atlético-MG", "Internacional", "Flamengo", "Bragantino",
                 "Santos", "São Paulo", "Ceará", "Botafogo", "Avaí", "Goiás",
                 "Cuiabá", "Coritiba", "América-MG", "Atlético-GO",
                 "Fortaleza", "Juventude")

print("Primeiros colocados:")
print(classificacao[:5])

print("Z4:")
print(classificacao[-4:])

print("Times participantes:")
print(sorted(classificacao))

print(f"O Avaí está na {classificacao.index('Avaí') + 1}º posição")
"""

"""
from random import randint
numran = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),)
print("Os valores sorteador foram",  end='')
for i in numran:
    print(f" {i}", end="")
print(f"\nO maior número entre eles é: {sorted(numran)[-1]}")
print(f"O menor número entre eles é: {sorted(numran)[0]}")
"""


"""
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
d = int(input("Digite o quarto número: "))

numeros = (a, b, c, d)
print(f"O número 9 apareceu {numeros.count(9)} vezes")

if numeros.count(3) > 0:
    print(f"O número 3 apareceu na primeira vez na posição {numeros.index(3) + 1}")
else:
    print("O número 3 não contém na tupla")

print("Números pares: ", end="")
for i in numeros:
    if i % 2 == 0:
        print(f" {i}", end="")
"""

"""
produtos = ("Lápis", 1.75, "Borracha", 2, "Caderno", 15.9, "Estojo", 25,
            "Transferidor", 4.20,"Compasso", 9.99, "Mochila", 120.32, "Livro", 34.90)

for pos, i in enumerate(produtos):
    if pos % 2 == 0:
        print(f"{i :.<30} R${produtos[pos+1]:.2f}")
"""

palavras = ("aprender", "orar", "pecar", "cometer", "amar", "notebook", "python")
for i in palavras:
    print(f"Na palavra {i} temos:", end="")
    for j in i:
        if j in "aeiou":
            print(f" {j}", end="")
    print("")
