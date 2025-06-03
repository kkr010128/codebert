import sys

data_list = sys.stdin.readlines()
data_length = int(data_list.pop(0))

for x in xrange(data_length):
	lines = map(int, data_list[x].strip().split())
	lines.sort(reverse = True)
	if lines[0]**2 == (lines[1]**2 + lines[2]**2):
		print "YES"
	else:
		print "NO"