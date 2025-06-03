N = int(input())
array = list(map(int, input().split()))
cnt = 0 
for i in range(N):
	minij = i 
	for j in range(i, N):
		if array[j] < array[minij]:
			minij = j 
	if minij != i:
		array[i], array[minij] = array[minij], array[i]
		cnt += 1

print(' '.join(map(str, array)))
print( "%d" % (cnt))

