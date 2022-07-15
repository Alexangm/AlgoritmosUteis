"""
sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input("Digite o sexo da pessoa: (M/F) ")).upper()
"""

"""
from random import randint

num = -1
numpc = randint(1, 10)
tent = 0
while num != numpc:
    num = int(input("Tente acertar o número que o computador pensou!\n >> "))
    tent += 1
    if(num != numpc):
        print("Você errou! Tente novamente!")
print(f"\n\nVocê acertou!!! Tentativas necessárias : {tent}")
"""

"""
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
op = -1
while op != 5:
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos números")
    print("[5] Sair")
    op = int(input(""))
    if op == 1:
        print(f"Soma = {n1 + n2}")
    if op == 2:
        print(f"Multiplicação = {n1 * n2}")
    if op == 3:
        if n1 > n2:
            print(f"{n1} é maior que {n2}")
        elif n2 > n1:
            print(f"{n2} é maior que {n1}")
        else:
            print(f"{n1} é igual a {n2}")
    if op == 4:
        n1 = int(input("Digite o novo primeiro valor: "))
        n2 = int(input("Digite o novo segundo valor: "))
"""

"""  while
n = num = int(input("Digite um número para calcular o fatorial: "))
res = 1
while num > 1:
    res = res * num
    num -= 1
print(f"Fatorial de {n} = {res}")
"""

"""for
n = int(input("Digite um número para ser calculado o fatorial: "))
if n == 0:
    res = 0
else:
    res = 1
for x in range(1, n+1):
    res = res * x
print(f"Fatorial de {n} = {res}")
"""

"""
ptermo = int(input("Digite o primeiro termo da sequência: "))
razao = int(input("Digite a razao da sequência: "))
i = 0
while i < 10:
    print(ptermo)
    ptermo = ptermo + razao
    i += 1
"""

"""
ptermo = int(input("Digite o primeiro termo da sequência: "))
razao = int(input("Digite a razao da sequência: "))
i = 0
j = 10
while i < j or j != 0:
    print(ptermo)
    ptermo = ptermo + razao
    i += 1
    if i == j:
        j = int(input("Quantos termos você quer mostrar a mais? "))
        i = 0
"""

"""
t = int(input("Qual o tamanho da sequência de Fibonacci a ser exibida? (min 2) "))
seq = [0, 1]
print("0\n1")
i = 2
while i < t:
    seq.append(seq[i-2] + seq[i-1])
    print(seq[i])
    i = i + 1
"""

"""
flag = 0
soma = 0
while flag != 999:
    soma = soma + flag
    flag = int(input("Digite 999: "))
print(f"Soma = {soma}")
"""

"""
maior = menor = num = soma = cont = 0
flag = ""
while flag != "N":
    num = int(input("Digite um número: "))
    soma = soma + num
    cont = cont + 1
    if flag == "":
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    flag = str(input("Continuar? ")).upper()
print(f"Maior = {maior}, menor = {menor}, média = {soma/cont}")
"""
