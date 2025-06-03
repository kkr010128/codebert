n = int(raw_input())
a = map(int, raw_input().split())

temp = 0
cnt = 0
for i in range(n):
	for j in range(n-i-1):
		if a[j] > a[j+1]:
			temp = a[j]
			a[j] = a[j+1]
			a[j+1] = temp
			cnt += 1

for i in range(n):
	if i != n-1:
		print(a[i]),
	else:
		print(a[i])

print cnt