data = input().split()
a = int(data[0])
b = int(data[1])
c = int(data[2])

if a > b or a < 1 or c > 10000:
	exit()

cnt = 0
for num in range(a,b+1):
	if (c%num) == 0:
		cnt += 1
print(cnt)
