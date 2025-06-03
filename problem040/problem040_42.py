a = input().split()
v = 2
while int(v) >= 1:
    if int(a[int(v)-1]) < int(a[int(v)]):
        pass
    else:
        b = int(a[int(v)-1])
        a[int(v)-1] = int(a[int(v)])
        a[int(v)] = int(b)
    v = int(v) - 1

if int(a[1]) < int(a[2]):
    pass
else:
    b = int(a[1])
    a[1] = int(a[2])
    a[2] = int(b)
print('%d %d %d' % (int(a[0]),int(a[1]),int(a[2])))
