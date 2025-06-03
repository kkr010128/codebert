h, w = map(int, input().split())
sheet = []

for j in range(h):
	lista = list(map(int, input().split()))
	lista.append(sum(lista))
	sheet.append(lista)

lista = []

for i in range(w+1):
	sum = 0
	for j in range(h):
		sum += sheet[j][i]
	lista.append(sum)
	
sheet.append(lista)

for i in range(h+1):
	text = ""
	for j in range(w+1):
		text += str(sheet[i][j]) + " "
	print(text[:-1])