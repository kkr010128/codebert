mod=10**9+7
n=int(input())
l=list(map(int,input().split()))
ans=1
rgb=[0,0,0]
for i in range(n):
    c=0
    for j in range(3):
        if l[i]==rgb[j]:
            c+=1
    if c==0:
        print(0)
        exit()
    p=rgb.index(l[i])
    if not 0<=p<=2:
        print(0)
        exit()
    rgb[p]+=1
    ans*=c
    ans%=mod
print(ans)
