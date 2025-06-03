#coding: UTF-8

l = raw_input()

a = int(l)
x = 1

while a != 0:
	print "Case %d: %d" %(x,a)
	x += 1

	l = raw_input()
	a = int(l)
	if l == 0:
		print "end"