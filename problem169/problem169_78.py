N = int(input())
A = [int(i) for i in input().split()]

P = [0]*N
for i in range(N-1):
    P[A[i]-1] += 1

for i in range(N):
    print(P[i])