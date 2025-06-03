import sys
write=sys.stdout.write
while True:
	h,w=map(int,raw_input().split())
	if h==w==0: break
	for i in xrange(h):
		l=[('#' if i%2==j%2==0 else ('.' if (i%2==1 and j%2==0) or (i%2==0 and j%2==1) else '#')) for j in xrange(w)]
		for i in l:
			write(i)
		print ""
	print ""