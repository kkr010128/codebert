t = raw_input()
s = t.split()
if s[0] == s[1]:
	print "a == b"
else:
	if int(s[0]) > int(s[1]):
		print "a > b"
	else:
		print "a < b"