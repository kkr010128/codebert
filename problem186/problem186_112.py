K, N = list(map(int, input().split()))
houses = list(map(int, input().split()))

min_dist = K
for i in range(N):
	if i == 0:
		dist = houses[-1] - houses[i]
	else:
		dist = houses[i] - houses[i-1]
		dist = K - dist
			
	if dist < min_dist:
		min_dist = dist
		
print(min_dist)