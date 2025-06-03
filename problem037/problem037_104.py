if __name__ == "__main__":
	s = int(input())
	m = s // 60
	h = str(m // 60)
	m = str(m % 60)
	s = str(s % 60)

	print(h + ":" + m + ":" + s)