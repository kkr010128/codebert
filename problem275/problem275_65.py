x,y = map(str,input().split())
a = {'1':300000,'2':200000,'3':100000}
if int(x) > 3 or int(y) > 3:
    if int(x) <= 3:
        print(a[x])
    elif int(y) <= 3:
        print(a[y])
    else:
        print(0)
else:
    if x == y == '1':
        print(1000000)
    else:
        print(a[x]+a[y])