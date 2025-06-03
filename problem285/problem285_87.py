s = input()
n = len(s)
a = [0]*(n+1)
yama = []
tani = []

for i in range(n):
	if s[i] == '<':
		a[i+1] = a[i] + 1

for i in range(n)[::-1]:
	if s[i] == '>':
		a1 = a[i+1] + 1
		if i != 0:
			if s[i-1] == '<':
				a[i] = max(a[i], a1)
			else:
				a[i] = a1
		else:
			a[i] = a1

ans = sum(a)
print(ans)