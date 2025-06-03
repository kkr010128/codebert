#coding: UTF-8

l = raw_input().split()

a = int(l[0])
b = int(l[1])



if 1 <= a and b <= 1000000000:
	d = a / b
	r = a % b
	f = float (a )/ b

	print "%d %d %f" %(d, r, f)