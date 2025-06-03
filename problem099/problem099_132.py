#coding:utf-8
import math

N,K = map(int,input().split())

A = [int(y) for y in input().split()]

Ma = max(A)
mi = 1

ans = Ma

def execute(f):
    count = 0
    for i in A:
        count += math.ceil(i / f) - 1
    if count <= K:
        return True
    else:
        return False

while True:
    median = (Ma + mi) // 2
    
    bobo = execute(median)
    
    if bobo:
        ans = min(ans,median)
        Ma = median
    else:
        mi = median + 1
    
    if Ma == mi:
        break

print("{}".format(ans))