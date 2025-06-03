s = raw_input()
s = s.lower().strip()
cnt = 0
while True:
	text = raw_input()
	if 'END_OF_TEXT' == text.strip():
		break
	text = text.lower()
	for item in text.split():
		if item == s:
			cnt += 1
print cnt