import sys
line = sys.stdin.readline()
n =[]
while line:
	if int(line) == 0:
		break;
	else:
		n.append(line)
	line = sys.stdin.readline()
c = 1
for i in n:
	print "Case",str(c)+":",str(i),
	c+=1