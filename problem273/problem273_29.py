N,K = map(int,input().split())
A = list(map(int,input().split()))
A = [(a-1) % K for a in A]
S = [0 for i in range(N+1)]
for i in range(1, N+1):
	S[i] = (S[i-1] + A[i-1]) % K

kinds = set(S)
counts = {}
ans = 0
for k in kinds:
	counts[k] = 0
for i in range(N+1):
	counts[S[i]] += 1
	if i >= K:
		counts[S[i-K]] -= 1
	ans += (counts[S[i]] - 1)
print(ans)