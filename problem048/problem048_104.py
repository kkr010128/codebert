# coding: utf-8
# Your code here!
n=int(input())
sum=0
min=1000001
max=-1000001
table=list(map(int,input().split(" ")))
for i in table:
    sum+=i
    if max<i:
        max=i
    if min>i:
        min=i

print(str(min)+" "+str(max)+" "+str(sum))
