import sys

S = sys.stdin.readline().strip()

N = 2019
L = len(S)
curr = 0
seen = {}
INV = 210
seen[curr] = 1
for i in range(L):
    curr = (curr * 10 + int(S[i])) % N
    t = (curr * pow(10, L-i, N)) %N
    if t not in seen: seen[t] = 0
    seen[t] += 1

res = 0
for i in range(N):
    if i not in seen: continue
    t = seen[i]
    res += t * (t-1)//2
print(res)