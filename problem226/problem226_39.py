h,n=map(int,input().split())
a=[int(x) for x in input().split()]
if sum(a) >= h:
    print("Yes")
else:
    print("No")