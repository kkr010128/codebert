import sys

n = int(raw_input())
#n = 30


for i in range(1, n+1):
	if i % 3 == 0:
		sys.stdout.write(" {:}".format(i))
	elif str(i).find('3') > -1:
		sys.stdout.write(" {:}".format(i))
print("")