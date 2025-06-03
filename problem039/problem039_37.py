def max(a,b):
	if a>b :
		return a
	else :
		return b

a,b,c = map(int,raw_input().split())
if a<b<c :
	print'Yes'
else :
	print'No'