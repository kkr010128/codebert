N,M=map(int,input().split())
A_M=list(map(int,input().split()))
if N >= sum(A_M):
    print(N-sum(A_M))
else:
    print(-1)