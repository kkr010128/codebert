n = int(input())
for _ in range(n):
	num = sorted(map(int, input().split()))
	print("YES" if num[2]**2 == num[1]**2 + num[0]**2 else "NO")