from bisect import bisect_left, bisect_right

H, W, M = map(int,input().split())
targets = [list(map(lambda x: int(x) - 1, input().split())) for i in range(M)]

cnth = [0] * H
cntw = [0] * W
wlist = [[] for i in range(H)]

for i in range(M):
	hi, wi = targets[i]
	cnth[hi] += 1
	cntw[wi] += 1
	wlist[hi].append(wi)

maxhi = []
maxwi = []
maxh = max(cnth)
maxw = max(cntw)

for i in range(H):
	wlist[i].sort()
	if cnth[i] == maxh:
		maxhi.append(i)
for i in range(W):
	if cntw[i] == maxw:
		maxwi.append(i)

for i in range(len(maxhi)):
	for j in range(len(maxwi)):
		if bisect_right(wlist[maxhi[i]], maxwi[j]) - bisect_left(wlist[maxhi[i]], maxwi[j]) == 0:
			print(maxh + maxw)
			exit()
print(maxh + maxw - 1)