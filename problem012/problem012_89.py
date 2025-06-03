import math
n = int(input())
cnt = 0
for i in range(n):
    x = int(input())
    if x == 2:
        cnt += 1
    elif x <= 1\
    or x % 2 == 0:
        continue
    else:
        j = 3
        prime = "yes"
        while j <= math.sqrt(x):
            if x % j == 0:
                prime = "no"
                break
            else:
                j += 2
        if prime == "yes":
            cnt += 1
print(cnt)