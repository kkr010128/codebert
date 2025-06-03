N = int(input())

S_list = []
for _ in range(N):
	S_list.append(input().strip())

data = []
for s in S_list:
	bottom = 0
	height = 0
	for c in s:
		if c == ")":
			height -= 1
			if bottom > height:
				bottom = height
		else:
			height += 1
	if height == 0:
		k1 = 1
		k2 = 0
	elif height > 0:
		k1 = 0
		k2 = -bottom
	else:
		k1 = 2
		k2 = bottom - height
	data.append((k1, k2, bottom, height, s))

data.sort()

def check():
	height = 0
	for k1, k2, b, h, s in data:
#		print(height, b, h, s)
		if height + b < 0:
			return False
		height += h
	return height == 0

if check():
	print("Yes")
else:
	print("No")

