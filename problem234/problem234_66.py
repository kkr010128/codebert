import collections
n = int(raw_input())
def g( a, b , n):
	count = 0
	## CASE 1
	if a == b and a <=n : 
		count +=1
	## CASE 2
	if a *10 + b <= n:
		count +=1
	
	if len(str(n)) <=2:
		return count

	## CASE 3
	s = str(n)
	if len(s) - 3 >= 1:
		count += 10 ** (len(s) - 3)

	## CASE 4

	s = str(n)
	if a == int(s[0]):
		m = s[1:-1]

		if m != '':

			#0,m-1
			count += int(m)
			if b <= int(s[-1]):
				count +=1
	elif a < int(s[0]):
		count += 10 ** (len(s) - 2)

	return count


h = collections.Counter()
for k in range(1, n+1):
	ks = str(k)
	a,b = int(ks[0]), int(ks[-1])
	h[(a,b)] +=1
s= 0
for a in range(1,10):
	for b in range(1,10):
		s += h[(a,b)] * h[(b,a)]

print s
