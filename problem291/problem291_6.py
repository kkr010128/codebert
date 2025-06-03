a = list(map(int,input().split()))
x = a[1]*2
if x>=a[0]:
    print(0)
else:
    print(a[0]-x)