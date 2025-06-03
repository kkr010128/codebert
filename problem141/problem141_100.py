n=int(input())
a=list(map(int,input().split()))
tot=sum(a)

v=[1]
for q in a:
    tot-=q
    v.append(min(2*(v[-1]-q),tot))
    
if all([u>=0 for u in v]):
    print(sum(v))
else:
    print(-1)