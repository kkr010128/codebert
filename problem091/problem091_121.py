N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0

for i in range(N-2):
	for j in range(i,N-1):
		for k in range(j,N):
			if L[i] + L[j] > L[k] and L[i]!=L[j] and L[j]!=L[k]:
				ans += 1

print(ans)
