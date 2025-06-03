x = input()
split_x = x.split()
a = int(split_x[0])
b = int(split_x[1])
c = int(split_x[2])

if a < b < c:
	print("Yes")
else:
	print("No")