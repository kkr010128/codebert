w = input().lower()
cnt = 0
while True:
	l = input()
	if l == 'END_OF_TEXT':
		break
	for e in l.split():
		cnt += e.lower() == w
print(cnt)

