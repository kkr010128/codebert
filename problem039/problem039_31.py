s = input().rstrip().split(' ')
a = int(s[0])
b = int(s[1])
c = int(s[2])

if a < b and b < c:
	print("Yes")
else:
	print("No")