import sys
n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for z in d:
	x, y = z
	if x == y:
		cnt += 1
		if cnt >= 3:
			print("Yes")
			sys.exit()
	else:
		cnt = 0
print("No")