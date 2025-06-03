N=int(input())
S=list(input() for _ in range(N))

from collections import Counter

cnt=Counter(S)
max_cnt=cnt.most_common()[0][1]
ans=[]
for k, v in cnt.items():
	if v!=max_cnt:
		continue
	ans.append(k)
print(*sorted(ans), sep="\n")