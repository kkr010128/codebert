n = input()
print "",
for i in range(1,n+1):
	if i % 3 ==0:
		print str(i),
	else:
		j = i
		while(j > 0):
			if(j%10==3):
				print str(i),
				break;
			j = j/10