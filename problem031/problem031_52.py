import statistics

while True:
	n = int(input())
	if n == 0:
		break
	
	str = input().split()

	list = []
	for i in range(n):
		list.append(int(str[i]))

	print(statistics.pstdev(list))