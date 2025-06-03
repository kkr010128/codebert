n = int(input())
a = map(int, input().split())
re = 0

from collections import Counter

c = Counter(a)

for i, v in c.items():
    if v >= 2:
        re += 1

if re >= 1:
    print("NO")
else:
    print("YES")
