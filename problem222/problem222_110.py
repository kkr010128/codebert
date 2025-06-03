from collections import Counter

n = int(input())
a = list(map(int, input().split()))

c = Counter(a)
new = c.values()

for i in new:
    if i != 1:
        re = "NO"
        break
    else:
        re = "YES"

print(re)
