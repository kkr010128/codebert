#coding:utf-8
import math

n = int(input())
prime_count = 0
for i in range(n):
    x = int(input())
    div = 1
    div_count = 0

    while div <= math.sqrt(x) and div_count < 3:
        if x % div == 0 and div == math.sqrt(x):
             div_count += 1
        elif x % div == 0 and div != math.sqrt(x):
             div_count += 2
        div += 1

    if div_count == 2:
        prime_count += 1

print(prime_count)