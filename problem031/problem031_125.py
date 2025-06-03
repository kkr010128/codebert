# coding: utf-8
# Your code here!
import math

while True:
    n = int(input())
    if n == 0:
        break
    s = list(map(int,input().split()))
    
    sum = 0
    for i in range(len(s)):
        sum += s[i]
    m = sum/len(s)
    
    a = 0
    for i in range(len(s)):
        a += s[i]*s[i]
    a = a/len(s)
    
    print("{0:.8f}".format(math.sqrt(a-m*m)))
