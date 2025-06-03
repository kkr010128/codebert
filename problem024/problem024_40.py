n, k = map(int, input().split())
pack = []
for i in range(n):
    pack.append(int(input()))

def trucks(p, k):
    t = 0
    c = 1
    for i in range(len(p)):
        if p[i] > k:
            return 1000000
        elif t + p[i] <= k:
            t += p[i]
        else:
            t = p[i]
            c += 1
    return c

minp = int(sum(pack) / k)
maxp = max(pack) * n
while minp < maxp - 1:
    p = int((maxp + minp) / 2)
    if trucks(pack, p) <= k:
        maxp = p
    else:
        minp = p

if trucks(pack, maxp - 1) <= k:
    print(maxp - 1)
else:
    print(maxp)
