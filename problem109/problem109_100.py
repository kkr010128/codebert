if __name__ == '__main__':

	n = int(input())

	S = [0,0,0,0]
	
	for _ in range(n):
		cmd = input()
		if cmd == "AC":
			S[0] += 1
		elif cmd == "TLE":
			S[2] += 1
		elif cmd == "WA":
			S[1] += 1
		else:
			S[3] += 1

	for i in range(4):
		if i == 0:
			print("AC x " + str(S[0]))
		elif i == 1:
			print("WA x " + str(S[1]))
		elif i == 2:
			print("TLE x " + str(S[2]))
		else:
			print("RE x " + str(S[3]))

