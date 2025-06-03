h= []
w= []
while True:
	a,b= map(int,input().split())
	if(not (a==0 or b==0)):
		h.append(a)
		w.append(b)
	elif(a==b==0):
		break
n= 0
for e in h:
	c= 0
	for f in range(e):
		if(w[n]%2==0):
			if(c== 0):
				print('#.'*(w[n]//2))
				c= 1
			else:
				print('.#'*(w[n]//2))
				c= 0
		else:
			if(c== 0):
				print('#.'*(w[n]//2)+'#')
				c= 1
			else:
				print('.#'*(w[n]//2)+'.')
				c= 0
	print()
	n+= 1