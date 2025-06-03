A,V = map(int,input().split())
B,W = map(int,input().split())
T = int(input())
d = abs(A-B)
dv = V-W
if dv<=0:
    print("NO")
else:
    if T*dv>=d:
        print("YES")
    else:
        print("NO")