"""
bd = []
bdpeso = []
count = int(0)

while True:
    nome = str(input("Digite o nome da pessoa: "))
    peso = float(input("Digite o peso da pessoa: "))
    bd.append([nome, peso])
    count += 1
    if "N" in str(input("Continuar [S/N] ? ")).upper():
        break

for i, pessoa in enumerate(bd):
    if i == 0 or bdpeso[0][1] > pessoa[1]:
        bdpeso.insert(0, pessoa)
    elif pessoa[1] > bdpeso[-1][1]:
        bdpeso.append(pessoa)
    else:
        for j in range(0, len(bd)-1):
            if pessoa[1] <= bdpeso[j][1]:
                bdpeso.insert(j, pessoa)
                break

print("Pessoas cadastradas, da mais leve pra mais pesada: ")
for pessoa in bdpeso:
    print(pessoa)
"""

"""
lista = [[], []]
for i in range(0, 7):
    num = int(input("Digite um número: "))
    if (num % 2 == 0):
        lista[0].append(num)
    else:
        lista[1].append(num)

for i, j in enumerate(lista):
    lista[i].sort()
    if i == 0:
        print(f"Pares: {j}")
    else:
        print(f"Ímpares: {j}")
"""

"""
matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f"Digite o valor para [{i}][{j}]: "))
        matriz[i].append(num)

for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]}] ", end='')
    print()
"""

"""
matriz = [[], [], []]
somapar = tercol = maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        num = int(input(f"Digite o valor para [{i}][{j}]: "))
        matriz[i].append(num)

for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]}] ", end='')
        if matriz[i][j] % 2 == 0:
            somapar += matriz[i][j]
        if j == 2:
            tercol += matriz[i][j]
    print()
print(f"Soma dos valores pares: {somapar}")
print(f"Soma dos valores da terceira coluna: {tercol}")
print(f"Maior valor da segunda linhas: {max(matriz[1])}")
"""

"""
from random import randint
from time import sleep
megasena = []
jogos = int(input("Quantos jogos você quer jogar? "))
for i in range(0, jogos):
    megasena.append([])

for i in range(0, jogos):
    for j in range(0, 6):
        num = randint(0, 60)
        if num not in megasena:
            megasena[i].append(num)
        else:
            j = j - 1
for i in range(0, jogos):
    print(f"Jogo {i+1}: ", end='')
    for j in range(0, 6):
        megasena[i].sort()
        print(f"[{megasena[i][j]:2}] ", end='')
    print()
    sleep(0.500)
print("Gl")
"""

"""
boletim = []

count = 0

while True:
    nome = str(input("Digite o nome: "))
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    boletim.append([nome, nota1, nota2])
    count += 1
    if "N" in (str(input("Continuar [S/N]? "))).upper():
        break

print(f"{'Nº':<4}{'Nome':<10}{'Média':<4}")
for i, aluno in enumerate(boletim):
    print(f"{i:<4}{aluno[0]:<10}{(aluno[1]+aluno[2])/2:<4.1f}")

while True:
    num = int(input("Mostrar nota de qual aluno [-1 para parar]? "))
    if num < 0:
        break
    print(f"Notas da {boletim[num][0]} são {boletim[num][1]} e {boletim[num][2]}")
"""

boletim = []

count = 0

while True:
    nome = str(input("Digite o nome: "))
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    boletim.append([nome, [nota1, nota2]])
    count += 1
    if "N" in (str(input("Continuar [S/N]? "))).upper():
        break

print(f"{'Nº':<4}{'Nome':<10}{'Média':<4}")
print('-'*18)
for i, aluno in enumerate(boletim):
    print(f"{i:<3}|{aluno[0]:<9}|{(aluno[1][0]+aluno[1][1])/2:<4.1f}")
print('-'*18)
while True:
    num = int(input("Mostrar nota de qual aluno [-1 para parar]? "))
    if num < 0:
        break
    print(f"Notas da {boletim[num][0]} são {boletim[num][1]}")

