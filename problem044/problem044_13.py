a,b,c = map(int,raw_input().split())
count = 0
if a == b :
	if c % a == 0:
		count += 1
else:
	for i in range(a,b+1):
		if c % i == 0:
			count += 1
print count 