N=int(input())
a=list(map(int,input().split()))
a_all=0
for i in range(N):
    a_all^=a[i]
ans=[]
for j in range(N):
    ans.append(a_all^a[j])
print(*ans)