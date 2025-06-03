# Belongs to : midandfeed aka asilentvoice
while(1):
	n = str(input())
	
	if n != '0':
		ans = 0
		for x in n:
			ans += int(x)
		print(ans)
	else:
		break