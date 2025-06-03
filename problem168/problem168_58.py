n,m=map(int,input().split())

a=list(map(int,input().split()))
cnt=0

for i in a:
    cnt+=i
   
if n-cnt<0:
    print(-1)

else:
    print(n-cnt)

