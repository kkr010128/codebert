n = int(raw_input())
card_list = 52*[0]

for i in range(0,n):
	(mark,rank) = map(str,raw_input().split())
	for j in range(0,4):
		if mark == 'SHCD'[j]:
			card_list[13*j+int(rank)-1] = 1

for i in range(0,52):
	if card_list[i] == 0:
		print '%c %d' %('SHCD'[i/13],i%13+1)