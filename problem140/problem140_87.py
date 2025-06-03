s = input()
a = [str(c) for c in s]
 
for i in range (len(a)-1):
	if a[i]=='?':
		if i!=0 and a[i-1]=='P':
			a[i]='D'
		elif a[i+1]=='D' or a[i+1]=='?':
			a[i]='P'
		else:
			a[i]='D'
if a[len(a)-1]=='?':
	a[len(a)-1]='D'
print(*a,sep='')