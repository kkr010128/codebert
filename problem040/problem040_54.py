n = input().split()
a = int(n[0])
b = int(n[1])
c = int(n[2])
if a > b:
	bf = a
	a = b
	b = bf
if b > c:
	bf = b
	b = c
	c = bf
if a > b:
	bf = a
	a = b
	b = bf
print(str(a) + " " + str(b) + " " + str(c))