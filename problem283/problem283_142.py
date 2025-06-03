# coding: utf-8
# Your code here!
N=int(input())

count=-1
for i in range(N//2+1):
    count+=1

if N%2==0:
    print(count-1)
else:
    print(count)