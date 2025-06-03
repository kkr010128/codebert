k= int(input())
s= input()

if len(s)>k:
	r=s[:k]+"..."
	print(r)
else: 
	print(s)