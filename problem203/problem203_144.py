import math

a, b = map(int, input().split())
cand = range(b*10, b*10+10)
out = -1
for el in cand:
    if math.floor(el * 0.08) == a:
        out = el
        break
    else:
        continue
print(out)