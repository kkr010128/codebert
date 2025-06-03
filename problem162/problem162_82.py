import math

n, m = map(int, input().split())
c = 0
f = [math.floor(n/2), math.floor(n/2) + 1]
if n % 2 == 0:
    while c < m:
        c += 1
        if c == math.floor(n/4) + 1:
            if (f[1] + 1) % n == 0:
                f[1] = n
            else:
                f[1] = (f[1] + 1) % n
        print(str(f[0]) + ' ' + str(f[1]))
        if (f[0] - 1) % n == 0:
            f[0] = n
        else:
            f[0] = (f[0] - 1) % n
        if (f[1] + 1) % n == 0:
            f[1] = n
        else:
            f[1] = (f[1] + 1) % n
else:
    while c < m:
        c += 1
        print(str(f[0]) + ' ' + str(f[1]))
        if (f[0] - 1) % n == 0:
            f[0] = n
        else:
            f[0] = (f[0] - 1) % n
        if (f[1] + 1) % n == 0:
            f[1] = n
        else:
            f[1] = (f[1] + 1) % n