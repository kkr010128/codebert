import math
n = int(raw_input())
cnt = 0
for i in range(n):
    j = 2
    num = int(raw_input())
    while j <= math.sqrt(num):
        if num % j == 0:
            break
        j+=1
    if j > math.sqrt(num):
        cnt+=1
print cnt
