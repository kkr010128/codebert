n, k = map(int, input().split(' '))
l = map(int, input().split(' '))

s = 1
if n == k:
	for i in l:
		s *= i
		s %= 1000000007
	print(s)
else:
	pos = []
	neg = []

	for i in l:
		if i >= 0:
			pos.append(i)
		else:
			neg.append(i)

	pos.sort()
	neg.sort(reverse=True)
	answer = []

	if k % 2 == 1 and not pos:
		for i in range(k):
			s *= neg[i]
			s %= 1000000007
		print(s)

	else:
		if k % 2 == 1:
			s = pos.pop()
		for i in range(k//2):
			if len(pos) >= 2:
				answer.append(pos.pop()*pos.pop())
			else:
				break
		for i in range(k//2):
			if len(neg) >= 2:
				answer.append(neg.pop()*neg.pop())
			else:
				break
		answer.sort(reverse=True)
		for i in range(k//2):
			s *= answer[i]
			s %= 1000000007
		print(s)