import sys

n = input()
for i in range(1,n+1) :
	if i%3==0 :
		print(' '),
		sys.stdout.write(str(i))
	else:
		x = i
		while(x>0):
			if(x%10==3):
				print(' '),
				sys.stdout.write(str(i))
				break
			else :
				x/=10
print('')