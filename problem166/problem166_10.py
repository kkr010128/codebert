from collections import Counter, defaultdict
a = defaultdict(int)
a[0] += 1
s = input()[::-1]
cur = 0
for i, x in enumerate(s):
    cur += (int(x)*pow(10, i, 2019))%2019
    cur %= 2019
    a[cur] += 1

def comb(a):
    return a*(a-1)//2

ans = 0
for x in a.values():
    if x >= 2:
        ans += comb(x)
print(ans)