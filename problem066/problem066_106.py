import sys

def shuffle(str, h):
	head = str[0:h]
	tail = str[h:]
	shuffled_str = tail + head
	return shuffled_str

#fin = open("test.txt", "r")
fin = sys.stdin

while True:
	str = fin.readline()
	str = str.rstrip("\n")

	if(str == "-"):
		break

	m = int(fin.readline())

	for i in range(m):
		h = int(fin.readline())
		str = shuffle(str, h)

	print(str)