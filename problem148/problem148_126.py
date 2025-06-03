A,B,C,K = map(int,input().split())

if A >= K:
	print(K)
elif B >= K - A:
	print(A)
elif C >= K - A - B:
	print(A - (K - A - B))