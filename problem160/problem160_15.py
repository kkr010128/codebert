from itertools import combinations_with_replacement

N, M, Q = map(int, input().split())
abcdn = [tuple(map(int, input().split())) for _ in range(Q)]

mx = 0
for AN in combinations_with_replacement(range(1, M+1), N):
	score = 0
	for a, b, c, d in abcdn:
		score += d if AN[b-1] - AN[a-1] == c else 0
	mx = max(score, mx)
print(mx)