import sys
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
n=int(input())
d=[]
for e in sys.stdin:
	e=int(e)
	if e in a:
		a[a.index(e)]=0
	if e in b:
		b[b.index(e)]=0
	if e in c:
		c[c.index(e)]=0
if sum(a)==0 or sum(b)==0 or sum(c)==0:
	print("Yes")
	exit()
for i in range(3):
	if a[i]==0 and b[i]==0 and c[i]==0:
		print("Yes")
		exit()
if (a[0]==0 and b[1]==0 and c[2]==0) or (a[2]==0 and b[1]==0 and c[0]==0):
	print("Yes")
	exit()
print("No")
