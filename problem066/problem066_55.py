while True:
	temp = input()
	if temp == '-':
		break
	else:
		cards = temp
		for i in range(int(input())):
			h = int(input())
			cards = cards[h:] + cards[:h]
	print(cards)