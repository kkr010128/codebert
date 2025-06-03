n=int(input())
a=list(map(int,input().split()))
if a[0]!=0:
    print(0)
    exit()
r=1
b=0
g=0
pos=3
for i in range(1,n):
    pre=0
    de=0
    if a[i]==r:
        pre += 1
        r += 1
        de=1
    if a[i]==b:
        pre += 1
        if de==0:
            b += 1
            de=1
    if a[i]==g:
        pre += 1
        if de==0:
            g += 1
    
    pos *= pre
print(pos%(10**9+7))
