def so(x):
	xx = int(x ** 0.5) + 1
	for i in range(2, xx):
		if x % i == 0:
			return True
	return False
    
x = int(input())
while(so(x)):
	x += 1
print(x)
