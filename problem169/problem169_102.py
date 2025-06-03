N = int(input())
A = [int(i) for i in input().split()]
d = {}
for i in range(1, N+1):
    d[i] = 0
for i in range(N-1):
    d[A[i]] += 1
for i in range(1, N+1):
    print(d[i])