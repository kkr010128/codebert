import sys
input = sys.stdin.buffer.readline

mod = 10**9 + 7

n,k = map(int,input().split())
a = list(map(int,input().split()))

se = []
hu = []

for e in a:
    if e > 0:
        se.append(e)
    elif e < 0:
        hu.append(-e)
se.sort()
hu.sort()

S = len(se)
H = len(hu)

Z = n - S - H

if Z + k > n:
    print(0)
    exit()

#negative個数の最小と最大
Hmi = max(0,k-Z-S)
Hma = min(k,H)

#正が無理なパターン
if Hmi == Hma and Hmi%2 == 1:
    if Z > 0:
        print(0)
    else:
        hu_mul = 1
        for i in range(Hmi):
            hu_mul = hu_mul*hu[i]%mod
        se_mul = 1
        for i in range(k-Hmi):
            se_mul = se_mul*se[i]%mod
        print((-hu_mul)*se_mul%mod)
else:
    se = se[::-1]
    hu = hu[::-1]
    hu_mul = 1
    se_mul = 1
    for i in range(Hmi):
        hu_mul = hu_mul*hu[i]%mod
    
    if Hmi%2 == 0:
        k -= Hmi
    else:
        hu_mul = hu_mul*hu[Hmi]%mod
        Hmi += 1
        k -= Hmi
    hidx = Hmi
    sidx = 0
    

    if k%2 == 1:
        if S == 0:
            print(0)
            exit()
        se_mul = se[0]
        sidx += 1
        k -= 1


    while k > 0:
        if hidx + 1 >= H and sidx + 1 >= S:
            print(0)
            exit()
        elif hidx + 1 >= H:
            se_mul = se_mul*(se[sidx]*se[sidx+1]%mod)%mod
            sidx += 2
        elif sidx + 1 >= S:
            hu_mul = hu_mul*(hu[hidx]*hu[hidx+1]%mod)%mod
            hidx += 2
        else:
            if hu[hidx]*hu[hidx+1] > se[sidx]*se[sidx+1]:
                hu_mul = hu_mul*(hu[hidx]*hu[hidx+1]%mod)%mod
                hidx += 2
            else:
                se_mul = se_mul*(se[sidx]*se[sidx+1]%mod)%mod
                sidx += 2
        k -= 2

    print((hu_mul)*se_mul%mod)



