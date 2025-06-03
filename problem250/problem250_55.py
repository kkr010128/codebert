import math
import sys
input = sys.stdin.readline

def isPrime(n):
    i = 2
    flag = True
    while i * i <= n:
        if n % i == 0:
            flag = False
            break
        else:
            i += 1
    return flag


x = int(input())

while True:
    if isPrime(x):
        print(x)
        break
    else:
        x += 1


