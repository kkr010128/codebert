a = map(int, raw_input().split())

for i in range(len(a)):
	point = a[i:].index(min(a[i:])) + i
	temp = a[i];
	a[i] = a[point]
	a[point] = temp
print '%s %s %s' % (str(a[0]), str(a[1]), str(a[2]))