l = list(input())
a = False
b = False
c = False


if l[0] == 'R':
	a = True
if l[1] == 'R':
	b = True
if l[2] == 'R':
  	c = True
    
if a and b and c:
  	print(3)
elif (a and b) or (b and c):
  	print(2)
elif a or b or c:
  	print(1)
else:
  	print(0)