from collections import defaultdict
n=int(input())
MAX=10000

d = defaultdict(int)

def col(x,y,z):
    if x == y and x == z  :
        return 1
    if x == y or y == z or z == x :
        return 3
    return 6

# x <= y <= z
for i in range(1,MAX):
    wkx = i**2
    if wkx > MAX:
        break
    for j in range(i,MAX):
        wky = wkx + j**2  + i * j
        if wky > MAX :
            break
        for k in range(j,MAX):
            wkz = wky + k**2 + i * k  + j * k
            if wkz > MAX :
                break
            d[wkz] = d[wkz] + col(i,j,k)
            
for i in range(n):
    k = i + 1
    print(d[k])
