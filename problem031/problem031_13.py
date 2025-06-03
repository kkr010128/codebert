import statistics

while True:
	n = int(input())
	if n == 0:
		break
	else:
		data = [float(s) for s in input().split()]
		print(statistics.pstdev(data))