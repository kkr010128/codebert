import math
n = int(input())
count = 0
for i in range(n):
    a = int(input())
    h = math.trunc(math.sqrt(a))+1
    b = 0
    if a == 1:
        b = 1
    if a == 2:
        b = 0
    elif a % 2 == 0:
        b = 1
    else:
        i = 3
        while i <= h:
            if a % i == 0:
                b = 1
            i += 2
    if b == 0:
        count += 1
print count