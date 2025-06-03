n = int(input())

i = 1
while i <= n:
    x = i
    if x % 3 == 0:
        print(" {:d}".format(i),end="")
    else:
        while x:
            if x % 10 == 3:
                print(" {:d}".format(i),end="")
                break
            x = x // 10
    i += 1
print("")
