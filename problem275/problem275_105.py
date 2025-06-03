x, y = map(int, input().split())

prise_dict = {3: 100000, 2: 200000, 1: 300000}
ans = 0
if x in prise_dict.keys():
    ans += prise_dict[x]
if y in prise_dict.keys():
    ans += prise_dict[y]
if x == y == 1:
    ans += 400000
print(ans)
