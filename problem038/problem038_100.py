#coding:utf-8

data = [int(i) for i in input().split()]
a = data[0]
b = data[1]
if a == b:
	print("a == b")
elif a > b:
	print("a > b")
else:
	print("a < b")