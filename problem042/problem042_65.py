tmp = -1
cnt = 1
output = []
while tmp != 0:
	tmp = int(input())
	if tmp == 0:
		break
	output += ["Case " + str(cnt) + ": " + str(tmp)]
	cnt += 1

for x in output:
	print(x)
