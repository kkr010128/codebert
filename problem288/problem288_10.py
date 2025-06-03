n=int(input())

ans=10**12
d=2
while d<=n**(1/2):
    if n%d==0:
        ans=min(ans,d+n//d-2)
    d+=1
if ans==10**12:
    print(n-1)
    exit()
print(ans)