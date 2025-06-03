v = 0
i = 0
a = []
b = []
while v == 0:
    x = input().split()
    if 0 == int(x[0]):
        if 0 == int(x[1]):
            v = 1
        else:
            a.append(int(x[0]))
            b.append(int(x[1]))
            i = int(i) + 1
        
    else:
        a.append(int(x[0]))
        b.append(int(x[1]))
        i = int(i) + 1
for j in range(int(i)):
    if a[j] < b[j]:
        pass
    else:
        c = a[j]
        a[j] = b[j]
        b[j] = c

for j in range(int(i)):
    print('%d %d' % (int(a[j]),int(b[j])))
