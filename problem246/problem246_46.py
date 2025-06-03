import itertools
import math

N = int(input())
M = math.factorial(N)
X = [i for i in range(1, N + 1)]
Y = list(itertools.permutations(X))

P = tuple([int(x) for x in input().split()])
Q = tuple([int(x) for x in input().split()])
for i in range(M):
    if Y[i] == P:
        a = i
    if Y[i] == Q:
        b = i

ans = abs(a - b)
print(ans)