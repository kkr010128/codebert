data = input().split()
W=int(data[0])
H=int(data[1])
x=int(data[2])
y=int(data[3])
r=int(data[4])
if (0 <= x - r <= W) and (0 <= x + r <= W):
	if (0 <= y - r <= H) and (0 <= y + r <= H):
		print("Yes")
	else:
		print("No")
else:
	print("No")