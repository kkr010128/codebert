from collections import Counter

n = int(input())
a = list(map(int, input().split()))
re = 0

c = Counter(a)
new = c.values()

for i in new:
    if i > 1:
        re += 1

if re > 0:
    print("NO")
else:
    print("YES")
