while True:
	num = input()
	if num == '0':
		break
	cnt = 0
	for i in num:
		cnt += int(i)
	print(cnt)