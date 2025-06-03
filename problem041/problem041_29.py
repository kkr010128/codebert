w, h, x, y, r = map(int, raw_input().split())
if x < r or y < r:
	print "No"
elif x+r>w or y+r>h:
	print "No"
else:
	print "Yes"