n=int(input())
p=list(map(int,input().split()))
res=p[0]
cnt=0
for i in p:
    if res>=i:
        cnt+=1
    res=min(res,i)
print(cnt)
