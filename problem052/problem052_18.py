x = int(input())
for i in range(1,x+1):
    y = i
    if y % 3 == 0:
        print(" %d" % i, end="")
        continue
    while True:
        if int(y) % 10 == 3:
            print(" %d" % i, end="")
            break
        y /= 10
        if int(y) == 0: break
print("")