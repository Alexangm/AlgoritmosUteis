# lista = []
# for i in range(0, 5):
#     lista.append(int(input(f"Digite o {i+1}º valor da lista ")))
# print(f"O maior valor da lista é o número {max(lista)}, que está na {lista.index(max(lista)) +1}ª posição")
# print(f"O menor valor da lista é o número {min(lista)}, que está na {lista.index(min(lista)) +1}ª posição")

"""
lista = []
for i in range(0, int(input("Quantos valores você quer digitar? "))):
    x = int(input("Digite o valor a ser inserido: "))
    if x in lista:
        print(f"{x} já está na lista!")
    else:
        lista.append(x)
lista.sort()
print(f"Você digitou os valores {lista}")
"""

"""
lista = list()
for i in range(0, 5):
    x = int(input("Digite um valor a ser inserido: "))
    if i == 0:
        lista.append(x)
    else:
        for j in range(0, len(lista)+1):
            if j == len(lista):
                lista.append(x)
                break
            if x < lista[j]:
                lista.insert(j, x)
                break
print(lista)
"""

"""
lista = []
for i in range(0, int(input("Quantos valores você quer digitar? "))):
    lista.append(int(input("Digite o valor a ser inserido: ")))

print(f"Você digitou {len(lista)} valores")

lista.sort(reverse=True)
print(f"De forma decrescente, sua lista é: {lista}")

if 5 in lista:
    print("O valor 5 está na lista!")
else:
    print("O valor 5 não está na lista!")
"""

"""
lista = []
listapar = []
listaimpar = []
for i in range(0, int(input("Quantos valores você quer digitar? "))):
    lista.append(int(input("Digite o valor a ser inserido: ")))
for i in lista:
    if i % 2 == 0:
        listapar.append(i)
    else:
        listaimpar.append(i)

print(f"Números pares: {listapar}")
print(f"Número ímpares: {listaimpar}")
print(f"Lista inteira: {lista}")
"""

expressao = str(input("Digite uma expressão matemática: ")).strip()
pa = pf = 0
pa = expressao.count("(")
pf = expressao.count(")")
if pa == pf:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está errada!")
