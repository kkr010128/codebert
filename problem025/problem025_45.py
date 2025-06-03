# coding: utf-8
# Here your code !
n=int(input())
A=[int(i) for i in input().split()]
q=int(input())
m=[int(i) for i in input().split()]


from itertools import combinations
x=[]
for i in range(len(A)):
    t=(list(combinations(A,i)))
    x.append(t)
combi=set()
for i in x:
    for j in i:
        combi.add(sum(j))

for i in m:
    if i in combi:
        print("yes")
    else:
        print("no")