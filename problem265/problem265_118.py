import math

N = int(input())
ans = -1
for i in range(N+1):
	if math.floor(i*1.08) == N:
		ans = i
if ans == -1:
	print(':(')
else:
	print(ans)