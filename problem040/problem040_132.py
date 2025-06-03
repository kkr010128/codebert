a,b,c = map(int,raw_input().split())

if a>b:
	tmp = a
	a = b
	b = tmp

if b>c:
	tmp = b
	b = c
	c = tmp

if a>b:
	tmp = a
	a = b
	b = tmp

print "%d %d %d" %(a,b,c)	