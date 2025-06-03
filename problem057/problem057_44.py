while(True):
	score = [int(i) for i in input().split()]
	if score[:] == [-1,-1,-1]:
		break
	if score[0] == -1 or score[1] == -1:
		print('F')
	else:
		score_sum = score[0] + score[1]
		if score_sum >= 80:
			print('A')
		elif 80 > score_sum >= 65:
			print('B')
		elif 65 > score_sum >= 50:
			print('C')
		elif 50 > score_sum >= 30:
			if score[2] >= 50:
				print('C')
			else :
				print('D')
		elif 30 > score_sum:
			print('F')