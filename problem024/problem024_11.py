n, k = map(int, raw_input().split())
w = []
max = 0
sum = 0
for i in xrange(n):
	w_i = int(raw_input())
	if w_i > max:
		max = w_i
	sum += w_i
	w.append(w_i)

def can_put(w, p, k):
	weight = 0
	cnt = 1
	for w_i in w:
		if weight + w_i <= p:
			weight += w_i
		else:
			cnt += 1
			if cnt > k:
				return 0
			else:
				weight = w_i
	return 1

low = max
high = sum

while low < high:
	mid = (low + high) / 2
	#print high, mid, low
	if can_put(w, mid, k) == 1:
		#print("*1")
		high = mid
	else:
		#print("*0")
		low = mid + 1
	#print high, mid, low
print high