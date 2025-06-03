#coding: utf-8

nums=list(map(int,input().split()))

a=nums[0]
b=nums[1]

if a>b:
    print("a > b")
elif a<b:
    print("a < b")
else:
    print("a == b")