L=[]
N= 0
while True:
	n= int(input())
	if(n==0):
		break
	L.append(n)
	N= N+1
	
for x in range(N):
	print("Case",str(x+1)+":",L[x])