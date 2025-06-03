def allocate(n,w,k,p):
	t=0
	c=1
	for i in range(n):
		if t + w[i] > p:
			t=0
			c+=1
			if c > k:
				return -1
		t+=w[i]
	return 0

n,k=map(int,input().split())
w=[0]*n
m=(1<<30)*-1
s=0
for i in range(n):
	w[i]=int(input())
	m=max(m,w[i])
	s+=w[i]

i=m
j=s
while (i<=j):
	guess = int(i+(j-i)/2)
	if allocate(n,w,k,guess) < 0:
		i = guess + 1
	else:
		j = guess - 1
print(i)

