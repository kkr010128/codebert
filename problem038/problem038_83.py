# coding: utf-8

num = input().rstrip().split(" ")

if int(num[0]) < int(num[1]):
    print("a < b")
elif int(num[0]) > int(num[1]):
    print("a > b")
else:
    print("a == b")