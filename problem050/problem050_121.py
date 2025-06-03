H=1
W=1
while H!=0 or W!=0:
	H,W = [int(i) for i in input().split()]
	if H!=0 or W!=0:
		for i in range(W):
			print('#',end='')
		print()
		for i in range(H-2):
			print('#',end='')
			for j in range(W-2):
				print('.',end='')
			print('#',end='\n')
		for i in range(W):
			print('#',end='')
		print('\n')