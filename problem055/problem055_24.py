import sys

nyuukyosha = []

for tou in range(4):
	nyuukyosha.append([])
	for kai in range(3):
		nyuukyosha[tou].append([])
		for heya in range(10):
			nyuukyosha[tou][kai].append(0)

n = int(raw_input())

for i in range(n):
	data = map(int, raw_input().split())
	a = data[0] - 1
	b = data[1] - 1
	c = data[2] - 1
	nyuukyosha[a][b][c] += data[3]

for tou in range(4):
	for kai in range(3):
		for heya in range(10):
			sys.stdout.write(" {:}".format(nyuukyosha[tou][kai][heya]))
		print("")
	if tou < 3:
		print("####################")