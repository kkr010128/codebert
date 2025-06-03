from itertools import combinations
while True:
	n,m=map(int,input().split())
	if n==m==0: break
	print(sum(1 for p in combinations(range(1,n+1),3) if sum(p)==m))