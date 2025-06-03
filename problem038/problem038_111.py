num = raw_input()
num = num.split()
a = int(num[0])
b = int(num[1])

if a < b:
	print "a < b"
elif a > b:
	print "a > b"
else:
	print "a == b"