# coding: utf-8
# Your code here!
import sys

n,k=map(int,input().split())
H=list(map(int,input().split()))
H.sort()
if n>k:
    for i in range(k):
        H[n-1-i]=0
else:
    print(0)
    sys.exit()
    
sum_H=sum(H)
print(sum_H)