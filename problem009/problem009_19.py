N = int(input())
E = [[] for _ in range(N+1)]
for _ in range(N):
	tmp = list(map(int, input().split()))
	if tmp[1] == 0:
		continue
	E[tmp[0]] = tmp[2:]

cnt = [0 for _ in range(N+1)]
q = [1]

while q:
	cp = q.pop(0)
	for np in E[cp]:
		if cnt[np] != 0:
			continue
		
		cnt[np] = cnt[cp] + 1
		q.append(np)

for ind, cost in enumerate(cnt):
	if ind == 0:
		continue
	if ind == 1:
		print(ind, 0)
	else:
		if cost == 0:
			print(ind, -1)
		else:
			print(ind, cost)
