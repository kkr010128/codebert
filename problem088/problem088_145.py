n = input()
a = list(map(int, input().split()))
min = a[0]
ans = 0            
for i in a:
	if min > i:
		ans += min - i
	else:
		min = i

print(ans) 