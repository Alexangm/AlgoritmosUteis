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
