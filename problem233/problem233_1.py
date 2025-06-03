N=int(input())
P=list(map(int,input().split()))
x=N+1
cnt=0

for i in range(N):
    if P[i]<x:
        cnt+=1
        x=P[i]
print(cnt)