from math import sqrt
n = int(input())
p = 0

for i in range(n):
    x = int(input())
    if x == 2:
        p += 1
    elif x%2 == 1:
        j=3
        f = 0
        while j < (int(sqrt(x))+1):
            if x%j == 0:
                f = 1
                break
            else:
                j += 2
        if f == 0:
            p += 1



print(p)
