n = int(input())
Tp = 0
Hp = 0
tmp = "abcdefghijklmnopqrstuvwxyz"
alph = list(tmp)

for i in range(n):
    Ta,Ha = input().split()
    lTa = list(Ta)
    lHa = list(Ha)
    num = 0

    if (len(Ta) <= len(Ha)):  #definition of num
        num = len(Ta)

    else:
        num = len(Ha)

    if (Ta in Ha and lTa[0] == lHa[0]): #drow a
        if (Ta == Ha):
            Tp += 1
            Hp += 1
        else:
            Hp += 3

    elif (Ha in Ta and Ha != Ta and lTa[0] == lHa[0]):
        Tp += 3


    else:
        for i in range(len(lTa)):  # convert alphabet to number
            for j in range(26):
                if (lTa[i] == alph[j]):
                    lTa[i] = int(j)

                else :
                    continue

        for i in range(len(lHa)):  # convert alphabet to number
            for j in range(26):
                if (lHa[i] == alph[j]):
                    lHa[i] = int(j)

                else :
                    continue

        for i in range(num):
            if (lTa[i] < lHa[i]):
                Hp +=3
                break
            elif (lHa[i] < lTa[i]):
                Tp +=3
                break
            elif (lHa[i] == lTa[i]):
                continue

print(Tp,Hp)

