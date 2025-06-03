def i():
	return int(input())
def i2():
	return map(int,input().split())
def s():
	return str(input())
def l():
	return list(input())
def intl():
	return list(int(k) for k in input().split())

n = i()
a = [int(i) for i in input().split()]

cnt = 1
ans = 0
for i in range(n):
	if a[i] == cnt:
		cnt += 1
	else:
		ans += 1
if cnt == 1:
	print(-1)
else:
	print(ans)
