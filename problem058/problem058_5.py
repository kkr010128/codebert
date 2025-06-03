while True:
    c=0
    x, y = map(int, input().split())
    if x == 0 and y== 0:
        break
    for i in range(1, x+1):
        for j in range(i+1, x+1):
            for k in range(j+1, x+1):
                if i+j+k == y:
                    c += 1
    print (c)
