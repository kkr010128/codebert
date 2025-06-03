n = int(input())

ans = 0
for i in range(1,n+1)[::-1]:
	head = str(i)[0]
	tail = str(i)[-1]
	length = len(str(i))
	if tail == '0':
		continue
	if head == tail:
		if length == 1:
			ans += 1
		elif length == 2:
			ans += 3
		else:
			ans += 3
			for j in range(3,length+1):
				if length > j:
					ans += 10**(j-2) * 2
				else:
					ans += 2 * (int(str(i)[1:length-1]) + 1)
	elif head < tail:
		if length > 2:
			ans += int('1' * (length-2)) * 2
	else:
		if length > 1:
			ans += int('1' * (length-1)) * 2
print(ans)
