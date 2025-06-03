N=int(input())
a=0
ans=float('inf')
x=list(map(int,input().split()))
for i in range(100):
    for j in range(N):
        a=a+(x[j]-i-1)**2
    #print(a)
    ans=min(ans,a)
    a=0
print(ans)
