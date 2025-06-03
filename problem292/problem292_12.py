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
d = intl()

ans = 0
for i in range(n):
	for j in range(i+1,n):
		ans += d[i]*d[j]
print(ans)