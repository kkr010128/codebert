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
a = intl()

for i in range(n):
	if a[i]%2 == 0:
		if a[i]%3 != 0 and a[i]%5 !=0:
			print("DENIED")
			exit()
print("APPROVED")