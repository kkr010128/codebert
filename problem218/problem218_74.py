N = int(input())
S = {}
c = 0
for _ in range(N):
	s = input()
	if s not in S:
		S[s] = 1
	else:
		S[s] += 1
	c = max(c, S[s])
ans = []
for k, v in S.items():
	if v == c:
		ans.append(k)
ans.sort()
for a in ans:
	print(a)
