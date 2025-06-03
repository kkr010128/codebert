n = input()
a = map(int,raw_input().split())
sum = a[0]
max = a[0]
min = a[0]
for i in range(1,n):
	sum += a[i]
	if min > a[i]:
		tmp = min
		min = a[i]
		a[i] = tmp
	if  a[i] > max:
		tmp = max
		max = a[i]
		a[i] = tmp
print str(min),str(max),str(sum)