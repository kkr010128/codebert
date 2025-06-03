# coding: utf-8
# Your code here!

num = int(input())

a=0
b=0

for _ in range(num):
    input2 = input().split()
    if input2[0]>input2[1]:
       a=a+3 
    elif input2[0]<input2[1]:
        b=b+3
    else:
        a=a+1
        b=b+1
print(a,b)
