h = []
w = []
while True:
    a,b = map(int, raw_input().split())
    h.append(a)
    w.append(b) 
    if a == 0 and b == 0:
        break

for h,w in zip(h,w):    
    if h == 0 and w == 0:
        break;
    else:
        r = "#"
        for x in xrange(w-1):
            r = r + "#"
        for x in xrange(h):
	    print r
    print