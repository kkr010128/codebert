k = int(input())
lun = [str(i) for i in range(1, 10)]
L = [str(i) for i in range(1, 10)]
nL = []
while len(lun) < 10 ** 5:
    for num in L:
        l = num[-1]
        lm = int(l) - 1
        lp = int(l) + 1
        nL.append(num + l)
        if lm >= 0:
            nL.append(num + str(lm))
        if lp < 10:
            nL.append(num + str(lp))
    lun.extend(nL)
    L = nL
    nL = []
lunlun = [int(x) for x in lun]
lunlun.sort()
print(lunlun[k-1])
