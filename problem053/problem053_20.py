input()
a = list(map(int, input().split()))

a.reverse()

print(a[0], end = "")
for i in a[1:]:
	print(" ", end = "")
	print(i, end = "")

print("")