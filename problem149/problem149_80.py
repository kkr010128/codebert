n , m , x = map(int ,input().split())

a = [(list(map(int,input().split()))) for _ in range(n)]

Sum = [0] * (m + 1)
mincost = 999999999

for bit in range(1 << n):
	tmpcost = 0
	Sum = [0] * (m + 1)
	flag = False
	for i in range(0 , n):
		if ((bit >> i) & 1):
			tmpcost += a[i][0]
			for j in range(1 , m + 1):
				Sum[j] += a[i][j]
	for i in range(1 , m + 1):
		if Sum[i] < x:
			flag = True
			break
	if flag == False:
		mincost = min(mincost , tmpcost)

if mincost == 999999999:
	print(-1)
else :
	print(mincost)