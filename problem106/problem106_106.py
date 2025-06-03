N = int(input())
 
V = [0]*10000
 
for j in range (1, 100):
	for k in range (1, 100):
		for l in range (1, 100):
			if j**2+k**2+l**2+j*k+k*l+j*l < 10001:
				V[j**2+k**2+l**2+j*k+k*l+j*l-1]+=1

for i in range (0, N):
	print(V[i])