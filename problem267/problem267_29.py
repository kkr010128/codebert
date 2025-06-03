from itertools import product

n = int(input())
s = input()
ans = 0
for a, b, c in product(map(str, range(10)), repeat=3):
    ai = s.find(a)
    bi = s.find(b, ai + 1)
    ci = s.find(c, bi + 1)
    if ai != -1 and bi != -1 and ci != -1:
        ans += 1
print(ans)
