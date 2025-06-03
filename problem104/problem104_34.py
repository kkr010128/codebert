l,r,d=map(int,input().split())
if l%d!=0:
    ans=(r//d)-(l//d)
else:
    ans=(r//d)-(l//d)+1
print(ans)