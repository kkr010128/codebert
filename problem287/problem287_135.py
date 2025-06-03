# coding: utf-8
# Your code here!
n=int(input())
flag=0
for i in range(1,10):
    if n%i==0:
        if 10>n/i:
            flag=1
if flag:
    print('Yes')
else:
    print('No')