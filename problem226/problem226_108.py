H,N = map(int,input().split())
A = list(map(int,input().split()))
All = sum(A)

if H - All > 0:
    print("No")
else:
    print("Yes")