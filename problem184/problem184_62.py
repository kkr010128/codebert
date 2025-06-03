a = input()

b = list(a)

if len(a) >= 6:
	if b[2] == b[3]:
		if b[4] == b[5]:
			print("Yes")
		else:
			print("No")
	else:
		print("No")
else:
	print("No")

