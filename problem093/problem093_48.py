N, K = map(int, input().split())
P = list(map(lambda x: int(x) - 1, input().split()))
C = list(map(int, input().split()))

maxscore = -(10 ** 18)

for st in range(N):
	cumsum = [0]
	now = st
	while(P[now] != st):
		now = P[now]
		cumsum.append(cumsum[-1] + C[now])
	cumsum.append(cumsum[-1] + C[st])
	
	m = len(cumsum) - 1
	loopsum = cumsum[-1]
	
	if loopsum < 0:
		maxscore = max(maxscore, max(cumsum[1:min(K + 1, m + 1)]))
		continue
	
	score = (K // m - 1) * loopsum
	extended_cumsum = cumsum + [cumsum[i] + loopsum for i in range(1, K % m + 1)]
	score += max(extended_cumsum)
	maxscore = max(maxscore, score)
print(maxscore)