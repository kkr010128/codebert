H, W, K = map(int,input().split())
S = []
ans = [["" for _ in range(W)] for __ in range(H)]
checkBerry = []
cake = 1
for i in range(H):
    s = input()
    S.append(s)
    flag = False
    for ss in s:
        if ss == "#":
            flag = True
    checkBerry.append(flag)

LS = []
n = 0
lss = []
while(n < H):
    lss.append(n)
    if (checkBerry[n] == True):
        LS.append(lss.copy())
        lss = []
    n += 1

if lss != []:
    LS[-1].extend(lss)

for ls in LS:
    i = 0
    for l in ls:
        if checkBerry[l] == True:
            i = l
    firstBerry = False
    for j in range(W):
        if(S[i][j] == "#" and firstBerry == False):
            firstBerry = True
        elif(S[i][j] == "#" and firstBerry == True):
            cake += 1

        for l in ls:
            ans[l][j] = str(cake)
    cake += 1


for a in ans:
    print(" ".join(a))




