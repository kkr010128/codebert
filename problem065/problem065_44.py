w = str(input()).lower()
ans = 0

while True:
	t = str(input())
	if t == 'END_OF_TEXT': break
	words = t.lower().split()

	for word in words:
		if word == w: ans += 1

print(ans)

