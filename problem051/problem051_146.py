import sys

while True :
	h,w = map(int,raw_input().split())
	if h==0 and w==0 :
		break
	else :
		for i in range(h):
			if i%2:
				for j in range(w):
					if j%2:
						if j==w-1:
							sys.stdout.write('#\n')
						else :
							sys.stdout.write('#')
					else :
						if j==w-1:
							sys.stdout.write('.\n')
						else :
							sys.stdout.write('.')
			else :
				for j in range(w):
					if j%2 :
						if j==w-1:
							sys.stdout.write('.\n')
						else :
							sys.stdout.write('.')
					else :
						if j==w-1:
							sys.stdout.write('#\n')
						else :
							sys.stdout.write('#')
		print''