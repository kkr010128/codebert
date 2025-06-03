import collections
N = int(input())
A = [int(_) for _ in input().split()]
C = collections.Counter(A)
d = sum([C[i] * (C[i] - 1) // 2 for i in range(N + 1)])
for a in A:
    print(d - C[a] + 1)
