n = int(input())
i = 1
while i <= n:
    if i%3 == 0:
        print(' ' + str(i), end="")
    else:
        num = i
        while 0 < num:
            if num % 10 == 3:
                print(' ' + str(i), end="")
                break
            num //= 10
    i += 1
print()