n,m = map(int,input().split())
a = list(map(int,input().split()))

b = [x for x in a if x >= sum(a)/4/m]

if len(b)>=m:
    print("Yes")
else:
    print("No")
