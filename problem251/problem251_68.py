import sys
input = sys.stdin.readline

(n, k), (r, s, p), t = map(int, input().split()), map(int, input().split()), input()[:-1]
d, res = {'r': p, 's': r, 'p': s}, 0
for i in range(k):
    b = False
    for j in range(i, n, k):
        if i == j: res += d[t[j]]; b = False; continue
        if (t[j] != t[j-k]) | b: res += d[t[j]]; b = False
        else: b = True
print(res)