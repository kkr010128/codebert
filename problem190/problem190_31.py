a=input()

b=len(a)

c=(b-1)/2

d=(b+1)/2

if a[:int(c)]==a[int(d):]:

	print("Yes")
else:
  	print("No")