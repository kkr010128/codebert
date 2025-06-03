all_N = []
while True:
	N = list(map(int, input().split(' ')))
	if N[0] == 0 and N[0] == 0:
		break
	all_N.append(N)

for i in range(len(all_N)):
	print('#' * all_N[i][1])
	for j in range(all_N[i][0]-2):
		print('#%s#' % ((all_N[i][1]-2) * '.'))
	print('#' * all_N[i][1])
	print('')