import sys

a = []

n, m = map(int, input().split())
for i in range(n):
    ai = list(map(int, input().split()))
    ai.append(sum(ai))
    a.append(ai)

for i in range(n):
    print(" ".join(list(map(str, a[i]))))

ai = []
for j in range(m + 1):
    s = 0
    for i in range(n):
        s += a[i][j]
    ai.append(s)

print(" ".join(list(map(str, ai))))