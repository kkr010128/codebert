import math
cnt = 0
N = int(input())
for n in range(N):
    i = int(input())
    if i == 2\
    or i == 3\
    or i == 5\
    or i == 7:
        cnt += 1
    elif i % 2 == 0:
        continue
    else:
        j = 3
        prime = 1
        while j >= 3 and j <= int(math.sqrt(i)):
            if i % j == 0:
                prime = 0
                break
                
            j += 2
        if prime == 1:
            cnt += 1

print(cnt)