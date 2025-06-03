N=int(input())
S=list(input() for _ in range(N))

from collections import Counter

cnt=Counter(S)
max_cnt=cnt.most_common()[0][1]
ans=[name for name, cnt in cnt.items() if cnt==max_cnt]
print(*sorted(ans), sep="\n") 