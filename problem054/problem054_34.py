n = int(input())
deck = []

for i in range(n):
	mark, num = input().split()
	deck.append((mark, int(num)))

for mark, num in [(mark, num) for mark in 'SHCD' for num in range(1,14) if (mark, num) not in deck]:
	print(mark, num)