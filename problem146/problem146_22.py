import math

mod = 1000000007
n = int(input())
zero = 0
dic = {}
dic[(0, 1.5)] = 0
dic[(1.5, 0)] = 0
for i in range(n):
    ai, bi = map(int, input().split())
    idx = (ai, bi)
    if ai < 0:
        ai, bi = -ai, -bi
    if idx == (0, 0):
        zero += 1
    elif idx[0] == 0:
        dic[(0, 1.5)] += 1
    elif idx[1] == 0:
        dic[(1.5, 0)] += 1
    else:
        g = math.gcd(abs(ai), abs(bi))
        ai = ai // g
        bi = bi // g
        idx = (ai, bi)
        if idx in dic:
            dic[idx] += 1
        else:
            dic[idx] = 1

ans = 1
already = set([])
for key, value in dic.items():
    if key in already: continue
    a, b = key
    if a == 1.5 or b == 1.5:
        pair1 = dic[(0, 1.5)]
        pair2 = dic[(1.5, 0)]
        ans = (ans * (pow(2, pair1, mod)+pow(2, pair2, mod)-1)) % mod
        already.add((0, 1.5))
        already.add((1.5, 0))
    else:
        if b > 0: idx = (b, -a)
        else: idx = (-b, a)
        if idx in dic:
            pair1 = dic[key]
            pair2 = dic[idx]
            ans = (ans * (pow(2, pair1, mod)+pow(2, pair2, mod)-1)) % mod
            already.add(key)
            already.add(idx)
        else:
            pair1 = dic[key]
            ans = (ans * pow(2, pair1, mod)) % mod
            already.add(key)

ans = (ans + zero - 1) % mod
print(ans)