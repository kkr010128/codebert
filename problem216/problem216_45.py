from collections import defaultdict
d = defaultdict(int)

N,M,L = map(int,input().split())
d[N] += 1
d[M] += 1
d[L] += 1
print(("No","Yes")[len(d)==2])
