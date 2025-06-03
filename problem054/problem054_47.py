n = input()
cards = []
for i in range(n):
	cards.append(raw_input().split())

marks = ['S', 'H', 'C', 'D']
for i in marks:
	for j in range(1, 14):
		if [i, str(j)] not in cards:
			print i, j