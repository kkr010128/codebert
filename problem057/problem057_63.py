while True:
	m,f,r=map(int,raw_input().split())
	if m==f==r==-1: break
	if m+f<30 or m==-1 or f==-1: print 'F'
	elif m+f>=80: print 'A'
	elif 65<=m+f: print 'B'
	elif 50<=m+f: print 'C'
	elif r>=50: print 'C'
	else: print 'D'