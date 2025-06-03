a = list(map(int,input().split()));

a[0],a[1] = a[1],a[0]
a[0],a[2] = a[2],a[0]

for i in range(3):
    print(a[i],end=' ');