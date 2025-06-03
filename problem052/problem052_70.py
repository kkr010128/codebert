n = int(input())
for i in range(1, n + 1):
    if i % 3 == 0:
        print(' ' + str(i), end='')
    else:
        s = str(i)
        if '3' in s:
            print(' ' + str(i), end='')
print('')