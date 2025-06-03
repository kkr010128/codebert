a=input()
n=int(input())
for i in range(n):
	b=input().split()
	if b[0]=='print':
		print(a[int(b[1]):int(b[2])+1])
	elif b[0]=='replace':
		a=a[:int(b[1])]+b[3]+a[int(b[2])+1:]
	elif b[0]=='reverse':
		c=(a[int(b[1]):int(b[2])+1])
		c=c[::-1]
		a=a[:int(b[1])]+c+a[int(b[2])+1:]
		
		
		
		
