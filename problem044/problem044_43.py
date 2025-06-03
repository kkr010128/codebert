deglist = raw_input().split(" ")
a = int(deglist[0])
b = int(deglist[1])
c = int(deglist[2])

cnt = 0
for x in range(a, b+1):
	if c % x == 0:
		cnt += 1

print cnt