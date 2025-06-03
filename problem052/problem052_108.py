n = int(input())
x = 1
print "",
while x <= n:
	if x%3==0:
		print str(x),
	else:
		t = x
		while t:
			if t%10==3:
				print str(x),
				t = 0
			else:
				t /= 10
	x += 1
print