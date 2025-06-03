# coding: utf-8
# Your code here!

n=int(input())
x=list(map(int,input().split()))
cost_min=1000000000
for i in range(1,101):
    cost=0
    for j in x:
        cost+=(j-i)**2
    if cost>=cost_min:
        continue
    cost_min=cost
print(cost_min)