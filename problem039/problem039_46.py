#coding:utf-8

a , b , c =input().rstrip().split(" ")

if int(a)<int(b):
    if int(b)<int(c):
        print("Yes")
    else:
        print("No")
else:
    print("No")