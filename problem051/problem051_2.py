import sys
while True:
	y,x=map(int, input().split())
	if x==y==0: break
	for i in range(1,y+1):
		for j in range(1,x+1):
			if(i%2==1):
				if(j%2==1):
					sys.stdout.write('#')
				elif(j%2==0):
					sys.stdout.write('.')
			if(i%2==0):
				if(j%2==0):
					sys.stdout.write('#')
				elif(j%2==1):
					sys.stdout.write('.')
		print('')
	print('')