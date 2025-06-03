#coding:utf-8
import math

def isPrime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3,math.ceil(math.sqrt(n))+1,2):
            if n % i == 0:
                return False
        return True

n = int(input())
c = 0
for i in range(n):
    if isPrime(int(input())):
        c += 1

print(c)