# Python 3
if __name__ == "__main__":
	input()
	str = input()
	a = [int(x) for x in str.split()]
	print(min(a), max(a), sum(a))