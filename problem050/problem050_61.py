while 1:
	H,W=map(int,raw_input().split())
	if H==W==0:break
	print(W*'#')
	while H>2:
		print('#'+(W-2)*'.'+'#')
		H=H-1
	print(W*'#'+'\n')