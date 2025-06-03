s=raw_input()
t=[]

for x in s:
	if x=='?':
		t.append('D')
	else:
		t.append(x)

print "".join(t)