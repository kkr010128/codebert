import math
while True:
	a_2 = 0
	n = int(input())
	if n == 0:
		break
	
	score = [int(x) for x in input().split()]
	m = sum(score)/len(score)
	#print(m)

	for i in range(len(score)):
		a_2 += (score[i]-m)*(score[i]-m)/n
		#print(a_2)
	print('%.4f'% math.sqrt(a_2))