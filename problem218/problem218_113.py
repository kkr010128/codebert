votos = dict()

quantidade = int(input())

for i in range(0, quantidade):
    nome = input()

    if(len(votos) == 0):
        votos[nome] = 1
    elif nome in votos:
            votos[nome] += 1
    else:
        votos[nome] = 1

maior = 0

for i in votos:
    if(votos[i] > maior):
        maior = votos[i]

nome = list()
for i in votos:
    if(votos[i] == maior):
        nome.append(i)

nome.sort()
for i in nome:
    print(i)