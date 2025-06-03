s = input()
p = input()

str2 = s + s
if str2.find(p) >= 0:
	print("Yes")
else:
	print("No")