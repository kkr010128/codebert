rooms = [0] * (4*3*10)
n = input();
for i in xrange(n):
	b,f,r,v = map(int, raw_input().split())
	rooms[(b-1)*30+(f-1)*10+(r-1)] += v

sep = "#" * 20
for b in xrange(4):
	for f in xrange(3):
			t = 30*b + 10*f
			print ""," ".join(map(str, rooms[t:t+10]))
	if b < 3: print sep