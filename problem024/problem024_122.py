import sys

def value(w,n,P):

	tmp_w = 0
	k = 1

	for i in range(n):
		if tmp_w + w[i] <= P:
			tmp_w += w[i]
		else:
			tmp_w = w[i]
			k += 1
	return k


def test():

	inputs = list(map(int,sys.stdin.readline().split()))
	n = inputs[0]
	k = inputs[1]
	w = []

	max = 0
	sum = 0

	for i in range(n):

		w.append(int(sys.stdin.readline()))

		if w[i] > max:
			max = w[i]

		sum += w[i]

	while max != sum:

		mid = (max + sum) // 2

		if value(w,n,mid) > k:
			max = mid + 1
		else:
			sum = mid


	print(max)

if __name__ == "__main__":
	test()

