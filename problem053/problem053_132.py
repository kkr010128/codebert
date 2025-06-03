n = int(input())
a = raw_input().split()
a.reverse()
for i in range(len(a)-1):
	print a[i],
print a[len(a)-1]