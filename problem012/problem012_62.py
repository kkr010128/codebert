from math import sqrt
n = int(input())
p = 0

for i in range(n):
    x = int(input())
    ad = 1
    j = 2
    while j < (int(sqrt(x))+1):
        if x%j == 0:
            ad = 0
            break
        else:
            j += 1
    p += ad



print(p)
