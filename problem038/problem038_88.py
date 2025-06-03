l = map(int, raw_input().split())
chr=""

if(l[0]==l[1]):
	chr="=="
elif(l[0]>l[1]):
	chr=">"
else:
	chr="<"

print "a %s b" % chr