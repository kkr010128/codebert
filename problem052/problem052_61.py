n = int(input())
for i in range(1,n+1):
    x = i
    if x % 3 == 0:
        print(' {}'.format(i), end='')
    else:
        while x:
            if x % 10 == 3:
                print(' {}'.format(i), end='')
                break
            else:
                x //= 10
print('')