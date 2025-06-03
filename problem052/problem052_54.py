n = int(input())
for i in range(1,n+1):
    if i % 3 == 0 or i % 10 == 3:
        print(" {}".format(i), end='')
    else:
        x = i
        while True:
            x = x // 10
            if x == 0:
                break
            elif x % 10 == 3:
                print(" {}".format(i), end='')
                break
print("")