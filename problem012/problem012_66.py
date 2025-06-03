import math
N = int(input())
count = 0
for _ in range(N):
    m = int(input())
    rm = int(math.sqrt(m))
    flag = 0
    for i in range(2,rm+1):
        if m %i ==0:
            flag = 1
            break
    if flag ==0 :count=count +1

print(count)