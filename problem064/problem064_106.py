
s1 = input()
s2 = input()

while len(s1) <= 100:
	s1 = s1 + s1

if s2 in s1:
	print("Yes")
else:
	print("No")


