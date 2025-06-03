import sys

#fin = open("test.txt", "r")
fin = sys.stdin

while True:
	[m, f, r] = list(map(int, fin.readline().split()))

	if m == -1 and f == -1 and r == -1:
		break

	sum_mf = m + f
	if m == -1 or f == -1:
		print("F")
	elif sum_mf >= 80:
		print("A")
	elif sum_mf >= 65:
		print("B")
	elif sum_mf >= 50:
		print("C")
	elif sum_mf >= 30:
		if r >= 50:
			print("C")
		else:
			print("D")
	else:
		print("F")