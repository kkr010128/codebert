while True:
	card=input()
	if card=='-':	break
	loop=int(input())
	for i in range(loop):
		ch=int(input())

		card=card[ch:]+card[:ch]
	print(card)