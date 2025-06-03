n = int(input())

taro = 0
hanako = 0
for _ in range(n):
	line = input().rstrip().split()

	if line[0] > line[1]: taro += 3
	elif line[0] < line[1]: hanako += 3
	else:
		taro += 1
		hanako += 1
print(taro, hanako)
