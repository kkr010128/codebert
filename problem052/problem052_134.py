# Python 3

def PrintI(i):
	print(" ", i)
	return i + 1

if __name__ == "__main__":
	n = input()
	n = int(n)
	s = ""
	for i in range(1, n + 1):
		if i % 3 == 0:
			s += " " + str(i)
		elif "3" in str(i):
			s += " " + str(i)
	print(s)