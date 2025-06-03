b = []
c = []
while True:
    inp = input()
    a = inp.split()
    a[0] = int(a[0])
    a[1] = int(a[1])
    if a[0] == 0 and a[1] == 0:
        break
    else:
        a.sort()
        b.append(a[0])
        c.append(a[1])
for i in range(len(b)):
    print(b[i],c[i])
