# Belongs to : midandfeed aka asilentvoice
while(1):
	s = str(input())
	if s == '-':
		break
	else:
		n = int(input())
		for _ in range(n):
			h = int(input())
			
			ans = s[h:] + s[:h]
			s = ans
			
		print(ans)