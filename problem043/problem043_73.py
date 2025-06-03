cnt = 1
output = []
while True:
	data = input().split()
	if data[0] == '0' and data[1] == '0':
		break
	elif int(data[0]) > int(data[1]):
		output += [data[1] + " " + data[0]]
	else:
		output += [data[0] + " " + data[1]]
for line in output:
	print(line)
