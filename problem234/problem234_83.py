import math

def makelist(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]

N = int(input())
sN = str(N)
l = len(sN)

ans = 0
for n in range(1, min(10, N+1)):
    sn = str(n)
    ans += 1
    
    cnt = 1
    for i in range(2, l):
        ans += cnt
        cnt *= 10

    if l == 2:
        if sN >= sn[-1] + sn[0]:
            ans += 1
    elif l > 2 and sN[0] >= sn[-1]:
        if sN[0] == sn[-1]:
            hoge = int(sN[1:-1])
            if sN[-1] < sn[0]:
                hoge -= 1
            ans += hoge + 1
        elif sN[0] > sn[-1]:
            ans += cnt

for n in range(11, N+1):
    sn = str(n)
    if sn[-1] != "0":
        if n > 10 and sn[0] == sn[-1]:
            ans += 1


        cnt = 1
        for i in range(2, l):
            ans += cnt
            cnt *= 10

        if l == 2:
            if sN >= sn[-1] + sn[0]:
                ans += 1
        elif l > 2 and sN[0] >= sn[-1]:
            if sN[0] == sn[-1]:
                hoge = int(sN[1:-1])
                if sN[-1] < sn[0]:
                    hoge -= 1
                ans += hoge + 1
            elif sN[0] > sn[-1]:
                ans += cnt

print(ans)
