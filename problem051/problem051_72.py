H=1
W=1
while H!=0 or W!=0:
	H,W = [int(i) for i in input().split()]
	if H!=0 or W!=0:
		for i in range(H):
			if i%2 == 0:
				for j in range(W):
					if j%2 == 0:
						print('#', end='')
					else:
						print('.', end='')
				print()
			else:
				for j in range(W):
					if j%2 == 0:
						print('.', end='')
					else:
						print('#', end='')
				print()
		print()