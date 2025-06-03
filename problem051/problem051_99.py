b = []
c = []
d = []
while True:
    a = input().split()
    a[0] = int(a[0])
    a[1] = int(a[1])
    if a[0] == 0 and a[1] == 0:
        break
    elif a[1]%2 == 0:
        b.append("#."*(a[1]//2)+"#")
        c.append((a[0],a[1]))
    else:
        b.append("#."*(a[1]//2)+"#.")
        c.append((a[0],a[1]))
for i in range(len(c)):
    if c[i][0]%2 == 0:
        for j in range(c[i][0]//2):
            print(b[i][0:-1])
            print(b[i][1:])
    else:
        for j in range(c[i][0]//2):
            print(b[i][0:-1])
            print(b[i][1:])
        print(b[i][0:-1])
    print("\n",end="")
