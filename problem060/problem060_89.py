a = input().split()
x = []
y = []
z = []
a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])
for i in range(a[0]):
    b = input().split()
    x.append(b)
    z.append([])
for i in range(a[1]):
    b  = input().split()
    y.append(b)
for i in range(a[0]):
    for j in range(a[2]):
        z[i].append(0)    
for i in range(a[0]):
    for j in range(a[2]):
        for k in range(a[1]):
            z[i][j] += int(x[i][k])*int(y[k][j])
for i in range(len(z)):
    for j in range(a[2]):
        z[i][j] = str(z[i][j])
for i in z:
    gam = " ".join(i)
    print(gam)
