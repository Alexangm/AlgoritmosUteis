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

"""
n = num = int(input("Digite um número para calcular o fatorial: "))
res = 1
while num > 1:
    res = res * num
    num -= 1
print(f"Fatorial de {n} = {res}")
"""