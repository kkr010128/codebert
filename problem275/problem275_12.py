x, y = map(int, input().split())

prise = {3: 100000, 2: 200000, 1: 300000}
ans = 0
if x in (1, 2, 3):
    ans += prise[x]
if y in (1, 2, 3):
    ans += prise[y]

print(ans + 400000 if x == y == 1 else ans)