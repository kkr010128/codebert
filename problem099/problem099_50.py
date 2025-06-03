n,k = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
x,y=0,10**9
while y>x+1:
    m = (x+y)//2
    c=0
    for i in l:
        c+=(i-1)//m
    if c<=k:
        y=m
    else:
        x=m
print(y)