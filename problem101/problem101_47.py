a, b, c = map(int, input().split())
k = int(input())
for x in range(k + 1):
	for y in range(k + 1):
		for z in range(k + 1):
			if a * 2**x < b * 2**y and b * 2**y < c * 2**z and x + y + z <= k:
				print("Yes")
				exit()
print("No")