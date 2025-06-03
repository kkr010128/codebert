import sys
while 1:
	H,W=map(int,raw_input().split())
	if H==0 and W==0:
		break;
	else:
		for h in range(H):
			for w in range(W):
				if h == 0 or w == 0 or h == H-1 or w == W-1 :
					sys.stdout.write('#')
				else:
					sys.stdout.write('.')

			sys.stdout.write('\n')
	sys.stdout.write('\n')