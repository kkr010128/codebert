s=raw_input()
target=raw_input()
ring=s+s[0:len(target)]
f=0

for i in range(len(s)):
	if ring[i:i+len(target)]==target:
		f=1
		break
if f==1:
	print "Yes"
else:
	print "No"