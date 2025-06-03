n = int(input())
ans = 0

for i in range(1,n+1):
	y = n//i
	g = i*(y*(y+1)//2)
	ans += g

print(ans)