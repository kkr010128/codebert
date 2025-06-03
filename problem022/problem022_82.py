def linearSearch(A, n, key):
	i = 0
	A.append(key)
	while (A[i] != key):
		i += 1
	del A[n]

	return i != n


if __name__ == '__main__':
	
	n = int(input())
	L = list(map(int, input().split()))

	q = int(input())
	Key = list(map(int, input().split()))

	cnt = 0
	for i in range(q):
		if (linearSearch(L, n, Key[i])):
			cnt += 1

	print(cnt)
