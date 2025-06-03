def merge(A, left, mid, right):
	n1 = mid - left
	n2 = right - mid
	L = []
	R = []
	for i in range(n1):
		L.append(A[left + i])
	for i in range(n2):
		R.append(A[mid + i])
	L.append(1000000001)
	R.append(1000000001)
	i = 0
	j = 0
	for k in xrange(left, right):
		global cnt
		cnt += 1
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1

def mergeSort(A, left, right):
	if left + 1 < right:
		mid = (left + right) / 2
		mergeSort(A, left, mid)
		mergeSort(A, mid, right)
		merge(A, left, mid, right)
	return A

n = int(raw_input())
S = map(int, raw_input().split())

cnt = 0
A = mergeSort(S, 0, n)

for i in xrange(len(A)-1):
	print(A[i]),
print A[len(A) - 1]
print cnt