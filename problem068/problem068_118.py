s = input()
for _ in range(int(input())):
	o = list(map(str, input().split()))
	a = int(o[1])
	b = int(o[2])
	if o[0] == "print":
		print(s[a:b+1])
	elif o[0] == "reverse":
		s = s[:a] + s[a:b+1][::-1] + s[b+1:]
	else:
		s = s[:a] + o[3] + s[b+1:]

