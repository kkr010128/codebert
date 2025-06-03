if __name__ == '__main__':

	n = input()

	ans = int(n[-1])
	if ans in [2,4,5,7,9]:
		print("hon")
	elif ans in [0,1,6,8]:
		print("pon")
	else:
		print("bon")
