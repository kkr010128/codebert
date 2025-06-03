n = int(input())
for i in range(3,n+1):
    x = i
    if x % 3 == 0:
        print(' {0}'.format(i), end='')
        continue

    while x != 0:
        if x % 10 == 3:
            print(' {0}'.format(i),end='')
            break
        x //= 10

print()