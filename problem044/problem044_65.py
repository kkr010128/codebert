a,b,c = map(int,input().split(" "))

ptn = 0

if a==b and a==c:
	print(1)
	ptn = 1

if a==b and a!=c:
	if a < c:
		print(1)
		ptn=2
	else:
		print(0)
		ptn=2

cnt = 0

for i in range(a,b+1):
	if c%i == 0:
		cnt += 1

if ptn != 1 and ptn != 2:
	print(cnt)