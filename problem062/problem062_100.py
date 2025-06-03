line = ""

while line != "0":
	line = input()
	x = 0
	for i in range(len(line)):
		x += int(line[i])
	if x != 0:
		print(x)

