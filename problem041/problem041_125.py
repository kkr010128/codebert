W,H,X,Y,R=map(int,input().split())
ok=True
if X<R or W-R<X:
    ok=False
if Y<R or H-R<Y:
    ok=False
if ok:
    print("Yes")
else:
    print("No")
