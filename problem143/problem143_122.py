K = int(input())
N = list(input())
#print(K,N)
ans = []
if len(N) > K:
	for i in range(len(N)-K):
		#print(i,len(N))
		N.pop(-1)
	N.append("...")
print("".join(N))
