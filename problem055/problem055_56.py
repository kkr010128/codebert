All = [[[0 for x in range(10)] for y in range(3)] for z in range(4)]

N = int(input())

i = 0
while i < N:
	b, f, r, v = map(int,input().split())
	All[b-1][f-1][r-1] += v
	i += 1

for x in range(4):
	for y in range(3):
		for z in range(10):
			print(" {}".format(All[x][y][z]), end = "")
			if z == 9:
				print("")
	if x != 3 and y == 2:
		for j in range(20):
			print("#", end = "")
		print("")