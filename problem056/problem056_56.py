n,m = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))

b = [0] * m
for i in range(m):
    b[i] = int(input())

from operator import mul
for i in range(n):
    print(sum(map(mul, A[i], b)))