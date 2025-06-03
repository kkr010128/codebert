n = [int(i) for i in input().split()]
N = n[0]
M = n[1]

A = [int(i) for i in input().split()]


A_sum = sum(A)

if A_sum > N:
    print(-1)
else:
    print(N - A_sum)