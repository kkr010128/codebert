def bingo(appear):
	for j in range(3):
		if appear[0][j] and appear[1][j] and appear[2][j]:
			return "Yes"
	for i in range(3):
		if appear[i][0] and appear[i][1] and appear[i][2]:
			return "Yes"
	if appear[0][0] and appear[1][1] and appear[2][2]:
		return "Yes"
	if appear[0][2] and appear[1][1] and appear[2][0]:
		return "Yes"
	return "No"


card = []
for _ in range(3):
	arr = list(map(int, input().split()))
	card.append(arr)
appear = [[False for _ in range(3)] for _ in range(3)]
n = int(input())
for _ in range(n):
	a = int(input())
	for i in range(3):
		for j in range(3):
			if a == card[i][j]:
				appear[i][j] = True

print(bingo(appear))