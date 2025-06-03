n = int(input())
info = []

for i in range(n):
    b, f, r, v = input().split()
    b = int(b)
    f = int(f)
    r = int(r)
    v = int(v)
    if info == []:
        info.append([b, f, r, v])
    else:
        for x in info:
            if b == x[0] and f  == x[1] and r == x[2]:
                x[3] += v
                isAdded = True
                break
            else:
                isAdded = False
        if isAdded == False:
            info.append([b, f, r, v])

for building in range(4):
    for floor in range(3):
        for room in range(10):
            print(" ", end = '')
            arePeople = False
            for y in info:
                if building + 1 == y[0] and floor + 1 == y[1] and room + 1 == y[2]:
                    print(y[3], end = '')
                    arePeople = True
            if arePeople == False:
                print("0", end = '')
        print('')
    if building < 3:
        print("####################")