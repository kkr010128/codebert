a,b,c,d=map(int,input().split())
X=[a,b]
Y=[c,d]
ans=-10**30
for x in X:
    for y in Y:
        if ans<x*y:
            ans=x*y
print(ans)

