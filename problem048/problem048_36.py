n = int(input())
a = input().split()
max = -1000000
min = 1000000
sum = 0
for i in range(0,n):
	sum = sum + int(a[i])
	if int(a[i]) > max:
		max = int(a[i])
	if int(a[i]) < min:
		min = int(a[i])

print(str(min) + " " + str(max) + " " + str(sum))