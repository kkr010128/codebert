s = int(input())
n = input()
x = n[0:s]
y = '...'
if s >= len(n):
	print(n)
else:
	print(x + y)