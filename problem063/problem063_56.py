tmp = "abcdefghijklmnopqrstuvwxyz"
alph = list(tmp)
alphcount = [0]*26

while True:
    try:
        letter = input()
        letterarray = list(letter.lower())
        # print(letterarray)

    except:
        break

    for x in letterarray:
        for i in range(26) :
            if (x == alph[i]):
                alphcount[i] += 1

            else :
                continue

for i in range(26):
    print(str(alph[i])+" : "+str(alphcount[i]))

