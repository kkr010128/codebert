n,x,t = map(int, input().split())

for i in range(1,1001):
	if n <= x * i:
		print(t*i)
		break