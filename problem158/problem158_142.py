k = int(input())
a, b = list(map(int, input().split()))
c = a / k
if c == int(c):
	print("OK")
else:
	d = int(c) + 1
	if (d*k) <=b:
		print("OK")
	else:
		print("NG")