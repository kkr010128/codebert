delta = int(input())
tri_all = []
for i in range(delta):
	tri = list(map(int, input().split(' ')))
	tri.sort()
	tri_all.append(tri)

for i in range(len(tri_all)):
	if tri_all[i][0]**2 + tri_all[i][1]**2 == tri_all[i][2]**2:
		print('YES')
	else:
		print('NO')