s = raw_input().rstrip().split(" ")
W = int(s[0])
H = int(s[1])
x = int(s[2])
y = int(s[3])
r = int(s[4])
if (x-r)>=0 and (x+r)<=W and (y-r)>=0 and (y+r)<=H:print "Yes"
else:print "No"