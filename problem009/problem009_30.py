n = int(input())

m = [[] for _ in range(n+1)]

for _ in range(n):
	tmp = [int(x) for x in input().split()]
	u,k,l = tmp[0],tmp[1],tmp[2:]
	m[u] += tmp[2:]
		
dp = [float('inf') for _ in range(n+1)]
dp[1] = 0
queue = [1]

while queue:
	t = queue.pop(0)
	for x in m[t]:
		if dp[x] > dp[t] + 1:
			dp[x] = dp[t] + 1
			queue.append(x)
			
for i,x in enumerate(dp):
	if i == 0:
		pass
	else:
		if x == float('inf'):
			print(i, -1)
		else:
			print(i, x)
			

	
