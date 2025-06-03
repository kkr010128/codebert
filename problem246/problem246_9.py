# coding: utf-8
# Your code here!

import itertools
n=int(input())
l = [i for i in range(1,n+1)]
a=list(map(int,input().split()))
b=list(map(int,input().split()))
cnt=1
ans_a=0
ans_b=0
for v in itertools.permutations(l):
    if list(v)==a:
        ans_a=cnt
    if list(v)==b:
        ans_b=cnt        
    if ans_a!=0 and ans_b!=0:
        break
    cnt+=1
print(abs(ans_a-ans_b))