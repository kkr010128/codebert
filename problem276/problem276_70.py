N = int(input())
A = list(map(int,input().split()))
tot = sum(A)
B = [0 for _ in range(N+1)]
for i in range(1,N+1):
    B[i] = B[i-1]+A[i-1]
cmin = abs(tot-2*B[1])
for i in range(2,N):
    cmin = min(cmin,abs(tot-2*B[i]))
print(cmin)