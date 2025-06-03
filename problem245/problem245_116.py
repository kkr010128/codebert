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
s = s()

cnt = 0
for i in range(n-2):
	if s[i]+s[i+1]+s[i+2] == "ABC":
		cnt += 1

print(cnt)