word = input().lower()
cnt = 0
while True:
	eot = input()
	if eot == 'END_OF_TEXT':
		break
	sent = eot.lower().split()
	if word in sent:
		cnt += sent.count(word)
print(cnt)