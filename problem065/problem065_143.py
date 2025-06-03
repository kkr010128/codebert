W = input().rstrip().lower()

ans = 0
while True:
	line = input().rstrip()

	if line == 'END_OF_TEXT': break
	
	line = line.lower().split(' ')
	for word in line:
		if word == W: ans += 1

print(ans)
