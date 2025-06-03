n=int(input())
a=list(map(int,input().split()))
s=sum(a)
res=0
m=1

for i in a:
    b=m-i
    if b<0:
        print(-1)
        exit(0)
    res+=i
    res+=b
    s-=i
    m=min(b*2,s)
print(res)
