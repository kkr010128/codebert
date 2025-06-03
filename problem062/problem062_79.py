#coding:utf-8
while True:
	l = [int(x) for x in input()]
	if len(l) and l[0]==0:
		break
	print(sum(l))