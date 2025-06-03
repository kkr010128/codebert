l,r,d = map(int, input().split())
var=l//d
var1=r//d
ans=var1-var
if l%d==0:
    ans+=1
print(ans)

