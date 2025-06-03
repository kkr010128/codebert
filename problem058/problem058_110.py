import sys

p = sys.stdin.readlines()
r = 0
for i in p:
	n,x = map(int,i.split())
	if n==0 and x==0:
		break
	else:
		for a in range(1,n+1):
			for b in range(1,n+1):
				if a==b:
					break
				else:
					for c in range(1,n+1):
						if a==c or b==c:
							break
						elif a+b+c==x:
							r+=1
	print r
	r = r*0