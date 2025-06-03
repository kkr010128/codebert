#coding:utf-8

def cal(a, b, op):
	if op=="+":
		return a + b
	elif op == "-":
		return a - b
	elif op == "*":
		return a * b
	elif op == "/":
		return a//b
	else:
		return -1

while True:
	buff = input().split()
	a = int(buff[0])
	b = int(buff[2])
	op = buff[1]
	if op == "?":
		break
	print(cal(a, b, op))