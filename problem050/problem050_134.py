while True:
	h,w=map(int,raw_input().split())
	if h==w==0: break
	for i in xrange(h):
		if i==0 or i==h-1: print '#'*w
		else: print '#'+'.'*(w-2)+'#'
	print ""