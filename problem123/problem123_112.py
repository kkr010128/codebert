from functools import reduce

N = int(input())
A = [int(x) for x in input().split()]
SUM=reduce(lambda a, b: a^b, A)

[print(SUM^A[i]) for i in range(N)]