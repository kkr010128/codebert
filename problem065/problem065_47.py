# Belongs to : midandfeed aka asilentvoice
w = str(input()).lower()
ans = 0
while(1):
	s = str(input())	
	if s == "END_OF_TEXT":
		break
	else:
		ans += sum([1 for x in s.split() if x.lower() == w])
		
print(ans)