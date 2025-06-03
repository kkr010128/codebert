#coding: Shift_JIS

def set_array(a,n):
	str=input()
	array=str.split()
	for i in range(n):
		a.append(int(array[i]))
	

n=int(input())
S=[]
set_array(S,n)
q=int(input())
T=[]
set_array(T,q)
C=0

def linear_search(S,x):
	S.append(x)
	l=len(S)
	i=0
	while(l>i):
		if S[i]==x:
			break
		i=i+1
	S.pop(-1)
	if i!=l-1:
		return 1;
	else:
		return 0;
for v in T:
	C+=linear_search(S,v)

print(C)
