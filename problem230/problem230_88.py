N, D, A = map(int, input().split())

data = []
for _ in range(N):
	data.append(tuple(map(int, input().split())))

data.sort()

queue = []
i = 0
j = 0
total = 0
height = 0
while i < N:
	if j >= len(queue) or data[i][0] <= queue[j][0]:
		x, h = data[i]
		i += 1
		if height < h:
			count = (h - height + A - 1) // A
			total += count
			height += count * A
			queue.append((x + D * 2, count * A))
	else:
		height -= queue[j][1]
		j += 1

print(total)
