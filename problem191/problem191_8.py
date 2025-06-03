l = int(input())
ll = float(l)
a=0
b=0
c=0

if(ll%3 == 0):
	a=ll/3
	b=ll/3
	c=ll/3
else:
	a=ll/3
	b=a
	c=ll-a-b

    
print(a*b*c)