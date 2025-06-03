N,K=map(int,input().split())
A=list(map(int,input().split()))
a=A[:]
for _ in range(K):
    t=[0]*(N+1)
    for i in range(N):
        ti=a[i]
        t[max(0,i-ti)]+=1
        t[min(N,i+ti+1)]-=1
    for i in range(N):
        t[i+1]+=t[i]
    a=t[:N]
    if min(a)==N:
        break
print(*a)