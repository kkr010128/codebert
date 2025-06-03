import numpy as np

N = int(input())
A = list(map(int,input().split()))

A = np.array(A)

A.sort()

d = {}

for a in A:
    d.setdefault(a,0)
    d[a] += 1



sieve = [True] * (A[-1] + 1)

for a in A:
    if d[a] > 1:
        sieve[a] = False
    for i in range(a + a, A[-1] + 1, a):
        sieve[i] = False

print(sum(1 for a in A if sieve[a]))