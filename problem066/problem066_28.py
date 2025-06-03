while True:
	deck = input()
	if deck == '-':
		break
	m = int(input())
	for i in range(m):
		n = int(input())
		deck = deck[n:] + deck[:n]
	print(deck)

