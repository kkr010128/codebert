datalist = []
Flag = True
for i in range(3000):
    if Flag:
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            Flag = False
        else:
            datalist.append((x, y))
#print(datalist)
for (i,j) in datalist:
    if i < j :
        print("{} {}".format(i, j))
    else:
        print("{} {}".format(j, i))

