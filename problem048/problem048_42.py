n = input()

if n != 0:
	l = [int(x) for x in raw_input().split()]		
	print min(l), max(l), sum(l)
else:
	print "0 0 0"