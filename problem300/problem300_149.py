import math
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

a, b = [int(i) for i in input().split()]
ma = gcd(a, b)
st = set()
for i in range(1, int(math.sqrt(ma) + 1)):
	if ma % i == 0:
		flg = True
		for j in st:
			if gcd(i, j) != 1:
				if i < j:
					st.remove(j)
					st.add(i)
				flg = False
				break
		if flg:
			st.add(i)
		flg = True
		ii = ma // i
		for j in st:
			if gcd(ii, j) != 1:
				if ii < j:
					st.remove(j)
					st.add(ii)
				flg = False
				break
		if flg:
			st.add(ii)
print (len(st))