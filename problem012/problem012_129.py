import math

loopnum = int(input())
cnt = 0
for i in range(loopnum):

	chknum = int(input())
	rootnum = int(math.sqrt(chknum))

	for j in range(2,rootnum+1):
		if chknum % j == 0:
			break
	else:
		cnt += 1

	# TLE
	#for j in range(2,chknum):
	#	if chknum % j == 0:
	#		break
	#else:
	#	cnt += 1

print(cnt)

