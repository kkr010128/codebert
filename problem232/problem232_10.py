a,b = map(str,input().split())
ans = ''
if int(a) > int(b):
	for _ in range(int(a)):
		ans += b
else:
	for _ in range(int(b)):
		ans += a
print(ans)