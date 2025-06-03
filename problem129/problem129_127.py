from collections import Counter
n = int(input())
a = sorted(map(int, input().split()))
c = Counter(a)
s = set()
for i in range(n):
    if a[i] in s:
        continue
    elif c[a[i]] >= 2:
        s.add(a[i])
    for j in range(2,10**6//a[i]+1):
        s.add(a[i]*j)
print(sum(not (ai in s) for ai in a))