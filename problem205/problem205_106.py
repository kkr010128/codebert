from collections import defaultdict as dict

n, p = map(int, input().split())
s = input()
a = []
for x in s:
    a.append(int(x))

def solve():
    l = [0]*p
    ans = 0
    for x in a:
        l_ = [0] * p
        for i in range(p):
            l_[(i * 10 + x) % p] += l[i]
        l, l_ = l_, l
        l[x % p] += 1
        ans += l[0]

    print(ans)
if p <= 5:
    solve()
    exit()
x = 0
mem = dict(int)
mem[0] = 1
ans = 0
a.reverse()
d = 1
for y in a:
    x += d*y
    x %= p
    d = (d * 10) % p
    ans += mem[x]
    mem[x] += 1
    # print(mem)

print(ans)