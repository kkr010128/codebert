b = []
c = []
while True:
    a = input().split()
    a[0] = int(a[0])
    a[1] = int(a[1])
    if a[0] == 0 and a[1] == 0:
        break
    else:
        b.append("#"*a[1])
        c.append(a[0])
for i in range(len(c)):
    for j in range(c[i]):
        print(b[i])
    print("\n",end="")
