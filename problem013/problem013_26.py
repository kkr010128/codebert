N = int(input())

RMax = 0
R = []


for i in range(N):
	r = int(input())
	if i == 0:
		rmi = r
	if i == 1:
		RMax = r - R[0]
	if i > 0:		
		rdif = (r - rmi)
		if rdif >= RMax:
			RMax = rdif
	R.append(r)
	if r < rmi:
		rmi = r

print(RMax)