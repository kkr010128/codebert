import sys
import math 

def be_able_to_convey(w, k, p):
	counter = 0
	cur_weight = 0
	for wi in w:
		if wi > p:
			return False

		cur_weight += wi
		if(cur_weight > p):
			cur_weight = wi
			counter += 1
			if(counter >= k):
				return False

	return True

#fin = open("test.txt", "r")
fin = sys.stdin

n, k = map(int, fin.readline().split())
w = [0 for i in range(n)]

for i in range(n):
	w[i] = int(fin.readline())
	
pmin = 1
pmax = int(10e9)

while pmin < pmax:
	p = math.ceil((pmin + pmax) / 2)
	if p == pmin or p == pmax:
		if be_able_to_convey(w, k, pmin):
			p = pmin
		else:
			#if not be_able_to_convey(w, k, pmax):
			#	print("error")
			p = pmax
		break

	if not be_able_to_convey(w, k, p):
		pmin = p
	else:
		pmax = p

print(p)