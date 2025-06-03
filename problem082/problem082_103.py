# abc177_b
s, t, match = input(), input(), 0
for i in range(len(s) - len(t) + 1):
	temp = 0
	for j in range(len(t)):
		if s[i + j] == t[j]:
			temp += 1
	if match < temp:
		match = temp
print(len(t) - match)