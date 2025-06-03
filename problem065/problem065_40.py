w = raw_input()
t = []

while 1:
	x = raw_input()
	if x =="END_OF_TEXT":break
	t+=x.lower().split()
print t.count(w)