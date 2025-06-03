X , Y = map(int,input().split())

a = 0
ans = "No"

for a in range(0,X+1):
	if (a * 2)+((X-a) * 4)==Y:
		ans = "Yes"
print(ans)