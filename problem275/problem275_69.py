a,b=map(int,input().split())
lst={0:0,1:300000,2:200000,3:100000}
if a>3:
    x=0
else:
    x=a
if b>3:
    y=0
else:
    y=b
if x==1 and y==1:
    ans=1000000
else :
    ans=lst[x]+lst[y]


print(ans)