#coding:utf-8

apartment = [[[0 for z in range(10)] for y in range(3)] for x in range(4)]
N = int(input())
data = [[int(x) - 1 for x in input().split()] for y in range(N)]
for x in data:
	apartment[x[0]][x[1]][x[2]] += x[3] + 1
	if apartment[x[0]][x[1]][x[2]] > 9:
		apartment[x[0]][x[1]][x[2]] = 9
	elif apartment[x[0]][x[1]][x[2]] < 0:
		apartment[x[0]][x[1]][x[2]] = 0
for x in range(4):
	for y in range(3):
		for z in range(10):
			print(" " + str(apartment[x][y][z]), end="")
		print()
	if x != 3:
		print(("#"*20))