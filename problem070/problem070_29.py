N,M=map(int,input().split())
#brr=[list(map(int,input().split())) for i in range(M)]
arr=[[] for i in range(N)]

check=[0]*N
ans=[]

for i in range(M):
    a,b=map(int,input().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)

q=[]
cnt=0
for i in range(N):
    if check[i]==0:
        cnt+=1
    q.append(i)
    #print(cnt,q)
    while q:
        x=q.pop()
        if check[x]==0:
            check[x]=1
            for j in arr[x]:
                q.append(j)
        
print(cnt-1)