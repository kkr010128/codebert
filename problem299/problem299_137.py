N = int(input())
A = list(map(int, input().split()))
D = {}
for i in range(N):
	i+=1
	D.update([(A[i-1], i)])

ans = []
for i in range(1, N+1):
	ans.append(D[i])

str_ans = list(map(str, ans))
print(' '.join(str_ans))