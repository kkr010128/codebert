A,V=map(int,input().split())
B,W=map(int,input().split())
T=int(input())
X=abs(B-A)
sp=V-W
Z=sp*T-X
if Z<0:
    print("NO")
else:
    print("YES")