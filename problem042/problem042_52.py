cases = []
n = 1
while n != 0:
	n = int(raw_input())
	if n == 0:
		continue
	cases.append(n)


for i in range(len(cases)):
	print "Case %d: %d" %(i + 1, cases[i])