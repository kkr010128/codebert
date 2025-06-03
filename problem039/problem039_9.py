#coding:utf-8

data = [int(i) for i in input().split()]
a = data[0]
b = data[1]
c = data[2]
if a<b<c:
	print("Yes")
else:
	print("No")