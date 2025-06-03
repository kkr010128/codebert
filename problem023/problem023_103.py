import sys

#fin = open("test.txt", "r")
fin = sys.stdin

n = int(fin.readline())
d = {}

for i in range(n):
	op, str = fin.readline().split()
	if op == "insert":
		d[str] = 0
	else:
		if str in d:
			print("yes")
		else:
			print("no")