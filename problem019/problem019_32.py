
pnum,mtime = map(int,input().split(" "))

total = [list(input().split(" ")) for _ in range(pnum)]

cnt=0
tcnt=0
while len(total) > 0:
	ztime = int(total[0][1]) - mtime
	if ztime <= 0:
		tcnt += int(total[0][1])
		print(total[0][0],int(tcnt))
		total.pop(0)
	else:
		total.append([total[0][0],ztime])
		total.pop(0)
		tcnt += mtime
	cnt += 1

