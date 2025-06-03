n = int(input())
data = []
[data.append(int(input())) for i in range(n)]

ans = data[1] - data[0]
x = data[0]

for d in data[1:]:
	ans = max(ans,d-x)
	x = min(d,x)

print(ans)