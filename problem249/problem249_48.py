a = [int(i) for i in input().split()]

if a[0]+a[1]<=a[2]:
    print(0,0)
elif a[0]>=a[2]:
    print(a[0]-a[2],a[1])
elif a[0]<a[2]:
    b = a[2]-a[0]
    print(0,a[1]-b)