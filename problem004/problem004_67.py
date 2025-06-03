# AOJ 0003 Is it a Right Triangle?
# Python3 2018.6.7 bal4u

for _ in range(int(input())):
	a, b, c = sorted(list(map(int, input().split())))
	print("YES" if a**2 + b**2 == c**2 else "NO")
