#inport
import sys
import numpy as np
from math import gcd

#input
K = int(sys.stdin.readline())
sum = 0
#3つ同じ場合..
sum = int((K+1)/2*K)
#print(sum)
#print(K) 
for i in range(1,K+1):
    for j in range(i+1,K+1):
        sum = sum + gcd(i,j) * 6
#        print(str(i) + ", " + str(j))
    #2つが同じ場合
        for l in range(j+1, K+1):
            sum = sum + gcd(gcd(i,j),l) * 6

print(int(sum)) 

