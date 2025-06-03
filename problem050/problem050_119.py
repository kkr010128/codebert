c = []

def listcreate():
    global c
    c = []
    for y in range(a[0]):
        b = []
        for x in range(a[1]):
            if y == 0 or y == a[0]-1 or x == 0 or x == a[1]-1:
                b.append("#")
            else:
                b.append(".")
        c.append(b)
    return

def listdraw():
    global c
    for y in range(len(c)):
        for x in range(len(c[0])):
            print(c[y][x], end='')
        print()
    return

for i in range(10000):
    a = list(map(int,input().split()))
    if sum(a)==0:
        break
    listcreate()
    listdraw()
    print()

