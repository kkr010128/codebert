n,k,s=map(int,input().split())

ans=[]
cnt=0
if s!=10**9:
    for i in range(n):
        if cnt<k:
            ans.append(s)
            cnt+=1
        else:
            ans.append(s+1)
else:
    for i in range(n):
        if cnt<k:
            ans.append(s)
            cnt+=1
        else:
            ans.append(1)
print(*ans)
