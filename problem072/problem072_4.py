n = int(input())

d = []

for i in range(n):
	d.append(list(map(int,input().split())))

cnt = 0
flag = 0

for i in range(n):
	if d[i][0] == d[i][1]:
		cnt = cnt + 1
	else:
		cnt = 0

	if cnt == 3:
		flag = 1

if flag == 1:
	print("Yes")
else:
	print("No")
