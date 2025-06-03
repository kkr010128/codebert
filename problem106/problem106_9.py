n = int(input())
ans = [0]*10**5
for i in range(1,int(n**0.5)):
	for j in range(1,int(n**0.5)):
		for k in range(1,int(n**0.5)):
			res = i**2 + j**2 + k**2 +i*j + j*k + k*i
			ans[res-1] += 1
for i in range(n):
	print(ans[i])