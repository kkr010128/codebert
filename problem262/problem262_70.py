n = int(input())
num_of_sug = []
sug = []
for i in range(n):
    m = int(input())
    num_of_sug += [m]
    sug += [[tuple(map(int, input().split())) for _ in range(m)]]

ans = 0

for i in range(2 ** n):
    liar = []
    honest = []
    for j in range(n):
        if ((i >> j) & 1):
            if j + 1 in liar:
                break
            elif j + 1 not in honest:
                honest += [j + 1]
            sug_tmp = sug[j]

            for sug_ in sug_tmp:
                if sug_[1] == 1:
                    if sug_[0] in liar:
                        break
                    elif sug_[0] not in honest:
                        honest += [sug_[0]]
                else:
                    if sug_[0] in honest:
                        break
                    elif sug_[0] not in liar:
                        liar += [sug_[0]]
            else:
                continue
            break
        else:
            if j + 1 in honest:
                break
            elif j + 1 not in liar:
                liar += [j + 1]
    else:
        if ans < len(honest):
            ans = len(honest)
print(ans)
