N,M = map(int,input().split())
A = list(map(int,input().split()))

a = sum(A)*(1/(4*M))
cnt = 0
for i in range(N):
    if A[i] >= a:
        cnt += 1

if cnt >= M:
    print("Yes")
else:
    print("No")