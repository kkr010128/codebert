origin_cards = raw_input()

while origin_cards != '-':
	
	shuffle_number = int(raw_input())

	for x in xrange(shuffle_number):
		h = int(raw_input())
		temp = origin_cards[h:len(origin_cards)+1] + origin_cards[0:h]
		origin_cards = temp
	print origin_cards

	origin_cards = raw_input()