x = raw_input().split()
a = x[0]
b = x[1]
c = x[2]

A = 0 

for i in range(int(a),int(b)+1):
	if int(c) % int(i) ==0:
		A += 1
	elif int(c) % int(i) != 0:
		A += 0
print A