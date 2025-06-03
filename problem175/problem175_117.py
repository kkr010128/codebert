n = int(input())
s = input()

from collections import Counter

a = [None] * n
for i in range(n):
    if s[i] == "R":
        a[i] = 0
    if s[i] == "G":
        a[i] = 1
    if s[i] == "B":
        a[i] = 2

c = [0] * 3
for v in a:
    c[v] += 1

ans = 1
for v in c:
    ans *= v

cnt = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        k = 2 * j - i
        if j < k and k < n:
            if s[i] == s[j]:
                continue
            if s[i] == s[k]:
                continue
            if s[j] == s[k]:
                continue
            cnt += 1

ans -= cnt

print(ans)
