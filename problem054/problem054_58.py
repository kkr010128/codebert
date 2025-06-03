cards = {
		"S": [0 for n in range(13)],
		"H": [0 for n in range(13)],
		"C": [0 for n in range(13)],
		"D": [0 for n in range(13)]
}
t = int(input())
for n in range(t):
	a,b = input().split()
	cards[a][int(b)-1] = 1

for a in ("S", "H","C", "D"):
	for b in range(13):
		if cards[a][b] == 0:
			print(a,b+1)