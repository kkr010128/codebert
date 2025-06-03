l = int(raw_input())
print "",
for i in range(l+1):
	if i//3 != 0:
		if i%3 ==0:
			print i,
		elif "3" in str(i):
			print i,