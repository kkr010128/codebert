s = str(input())
p = str(input())
if p[0] not in s:
	print("No")
elif p in s:
	print("Yes")
else:
	for i in range(len(s)):
		s = s[1:] + s[:1]
		if p in s:
			print("Yes")
			break
	else:
		print("No")
