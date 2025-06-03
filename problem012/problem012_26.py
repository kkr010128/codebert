import sys
import math

count = 0
judge = 0

for line in sys.stdin.readlines():
    num = int(line.strip())
    if judge == 0:
        judge = 1
    else:    
        flag = 0
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                flag = 1
                break
        if flag == 0:
            count += 1

print count