import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, K, C = [int(x) for x in input().strip().split()]
S = [i == 'o' for i in list(input().strip())]

a = [0] * K
b = [2 * 10 ** 5] * K
c = 0
k = 0
for i, s in enumerate(S, start=1):
    if c > 0:
        c -= 1
        continue
    if s:
        a[k] = i
        k += 1
        c = C
    if k == K:
        break

c = 0
k = 0
for i, s in enumerate(S[::-1], start=1):
    if c > 0:
        c -= 1
        continue
    if s:
        b[K-k-1] = N-i+1
        k += 1
        c = C
    if k == K:
        break

for aa, bb in zip(a, b):
    if aa == bb:
        print(aa)