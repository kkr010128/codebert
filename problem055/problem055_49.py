data = []
for i in xrange(4):
	tou = []
	data.append(tou)
	for j in xrange(3):
		kai = [0 for k in xrange(10)]
		tou.append(kai)
n = int(raw_input())
for i in xrange(n):
	b,f,r,v = map(int, raw_input().split(" "))
	data[b-1][f-1][r-1] = max(0, data[b-1][f-1][r-1] + v)
for tou in data:
	if not tou is data[0]:
		print "#" * 20
	for kai in tou:
		print " " + " ".join(map(str, kai))