a = int(input())
for i in range(1,a+1):
    x = i
    if i % 3 == 0 or i % 10 == 3:
        print(" {}".format(i), end = "")
    else:
        while int(x) > 0:
            x /= 10
            if int(x) % 10 == 3:
                print(" {}".format(i), end = "")
                break
print()
