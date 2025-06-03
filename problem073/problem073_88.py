import sys, os.path
import math
from collections import Counter
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")
 
 
 
MAX = 1000001
 
factor = [0]*(MAX + 1)
 
def generatePrimeFactors():
    factor[1] = 1
    for i in range(2,MAX):
        factor[i] = i
    for i in range(4,MAX,2):
        factor[i] = 2
    i = 3
    while(i * i < MAX):
        if (factor[i] == i):
            j = i * i
            while(j < MAX):
                if (factor[j] == j):
                    factor[j] = i
                j += i
        i+=1
 
 
def calculateNoOFactors(n):
    if (n == 1):
        return 1
    ans = 1
    dup = factor[n]
    c = 1
    j = int(n / factor[n])
    while (j > 1):
        if (factor[j] == dup):
            c += 1
        else:
            dup = factor[j]
            ans = ans * (c + 1)
            c = 1
        j = int(j / factor[j])
    ans = ans * (c + 1)
 
    return ans
generatePrimeFactors()
 
n = int(input())
temp = n
c = 1
count = 0
while(temp-c > 0):
    w = temp-c
    count += calculateNoOFactors(w)
    c += 1
print(count)