W,H,x,y,r = map(int ,raw_input().split())
#print ' '.join(map(str,[W,H,x,y,r]))

if x < W and 0 < x and 0<y and y < H and r <= x and r <= (H - x) :
	print "Yes"
else:
	print "No"