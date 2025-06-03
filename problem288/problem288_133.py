import math
n = int(input())
i = 1
tmp = n-1
while i <= math.sqrt(n):
    if n%i == 0:
        j = n//i
        if i + j < tmp:
            tmp = i + j -2
        else:
            pass
    else:
        pass
    i += 1
print(tmp)