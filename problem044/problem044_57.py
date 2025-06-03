data = input().split()
a = int(data[0])
b = int(data[1])
c = int(data[2])
divisor = list()
for i in range(a,b+1):
	if c % i == 0:
		divisor.append(i)

print(str(len(divisor)))