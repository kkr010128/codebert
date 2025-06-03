h = int(input())
cnt = 1
if h == 1:
	print(1)
	exit()
    
while(True):
	cnt += 1
	h = int(h / 2)
	if h == 1:
		break
print(2 ** cnt - 1)