
if __name__ == "__main__":
	while True:
		score = [int(i) for i in input().split()]
		if score[0] == score[1] == score[2] == -1:
			break
		if score[0] == -1 or score[1] == -1:
			print ('F')
		else:
			if score[0] + score[1] >= 80:
				print ('A')
			elif score[0] + score[1] >= 65:
				print ('B')
			elif score[0] + score[1] >= 50:
				print ('C')
			elif score[0] + score[1] >= 30:
				if score[2] == -1:
					print ('D')
				else:
					if score[2] >= 50:
						print ('C')
					else:
						print ('D')
			else:
				print ('F')