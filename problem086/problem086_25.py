N,X,T=map(int,input().split())

count = 0
ans = 0
while count < N:
	count += X
	ans +=T

print(ans)