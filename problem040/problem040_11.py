
'''
l = input().split()

l = list(map(int, l))
a,b,c = l[0],l[1],l[2]
'''
a,b,c = map(int, input().split())
if a > b:
	a,b = b,a

if b > c:
	b,c = c,b
	
if a > b:
	a,b = b,a
	
print(a,b,c)
