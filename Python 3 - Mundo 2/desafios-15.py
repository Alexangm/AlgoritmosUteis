"""
cont = flag = sum = 0
while True:
    flag = int(input("Digite um valor (999 para parar): "))
    if flag == 999:
        break;
    cont += 1
    sum += flag
print(f"A soma dos {cont} valores resultou em {sum}.")
"""

"""
while True:
    print("-"*30)
    num = int(input("Quer ver a tabuada de qual valor? "))
    if num < 0:
        break
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
    print("-" * 30)
print("→←"*15)
print("Acabou")
"""

"""
from random import randint

print("-" * 30 + "\n" + f"{'Par ou ímpar?':-^30}" + "\n" + "-" * 30)
vit = 0

while True:
    pc = randint(1, 10)
    jogador = int(input("Digite um valor: "))
    palpite = str(input("Você quer par ou ímpar? [I/P] "))
    duelo = (pc + jogador) % 2
    print(f"Você jogou {jogador} e o computador {pc}. Total de {jogador + pc}")

    if palpite == "P" or palpite == "p":
        if duelo == 0:
            print("Deu par, você venceu!")
            vit += 1
        else:
            print("Deu ímpar, você perdeu!")
            break
    elif palpite == "I" or palpite == "i":
        if duelo == 1:
            print("Deu ímpar, você venceu!")
            vit += 1
        else:
            print("Deu par, você perdeu!")
            break
    print("Vamos jogar novamente!\n")
print(f"Game Over! Total de vitórias = {vit}")
"""

"""
idade = cont = h = m20 = 0
sexo = str(" ")
c = " "

while True:
    sexo = str(" ")
    c = " "
    idade = int(input("Digite a idade: "))
    while sexo not in "mMhH":
        sexo = str(input("Informe o sexo [M/H]: ")).strip()
    if idade >= 18:
        cont += 1
    if sexo == "h":
        h += 1
    if sexo == "m" and idade < 20:
        m20 += 1
    while c not in "sSnN":
        c = str(input("Continuar? [S/N]: "))
    if c == "N" or c == "n":
        break
print(f"Total de pessoas com mais de 18 anos: {cont}")
print(f"Total de homens cadastrados: {h}")
print(f"Total de mulheres com menos de 20 anos: {m20}")
"""


"""
nome = c = " "
nomebarato = ""
preco = sum = barato = float(0)
cont10 = int(0)

while True:
    nome = str(input("Informe o nome do produto: ")).strip()
    preco = float(input("Informe o preço do produto: "))
    sum += preco
    if preco > 1000:
        cont10 += 1
    if nomebarato == "":
        barato = preco
        nomebarato = nome
    if preco < barato:
        barato = preco
        nomebarato = nome
    c = " "
    while c not in "sSnN":
        c = str(input("Continuar? [S/N]: "))
    if c == "N" or c == "n":
        break

print("•"*30)
print(f"Total gasto na compra: {sum}")
print(f"{cont10} produto/s custa/m mais que 1000 reais!")
print(f"{nomebarato} é o produto mais barato, custando {barato} reais")
"""

"""
nota50 = nota20 = nota10 = nota1 = 0
valori = valor = int(input("Digite o valor a ser sacado: "))
if valor // 50 > 0:
    nota50 = valor // 50
    valor = valor % 50
if valor // 20 > 0:
    nota20 = valor // 20
    valor = valor % 20
if valor // 10 > 0:
    nota10 = valor // 10
    valor = valor % 10
if valor // 1 > 0:
    nota1 = valor // 1
    valor = valor % 1
print(f"{valori} reais equivalem à:")

if nota50 > 0:
    print(f"Notas de 50 = {nota50}")
if nota20 > 0:
    print(f"Notas de 20 = {nota20}")
if nota10 > 0:
    print(f"Notas de 10 = {nota10}")
if nota1 > 0:
    print(f"Notas de 1 = {nota1}")
"""
