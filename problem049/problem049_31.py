H=1
W=1
while H!=0 or W!=0:
	H,W = [int(i) for i in input().split()]
	if H!=0 or W!=0:
		for i in range(H):
			for j in range(W):
				print('#',end='')
			print()
		print()