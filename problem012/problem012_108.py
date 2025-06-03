# coding: utf-8
# Here your code !
import math
i = input()
count=0

def isPrime(x):
    global count
    if x == 2:
        return True
    if x>2 and x%2==0:
        return False
    i = 3
    while i<=math.sqrt(x):
        if x%i==0:
            return False
        i+=2
    return True

for j in range(int(i)):
    j=int(input())
    if isPrime(j):
        count+=1
print(count)