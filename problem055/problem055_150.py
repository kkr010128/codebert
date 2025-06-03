import sys
n = input()
a = [[[0]*10 for i in range(3)] for i in range(4)]
for i in xrange(n):
	b = map(int, raw_input().split())
	a[b[0]-1][b[1]-1][b[2]-1] += b[3]

for i in range(4):
	for j in range(3):
		for k in range(10):
			sys.stdout.write(' %s' % a[i][j][k])
		print ""
	if i != 3:
		print '#'*20