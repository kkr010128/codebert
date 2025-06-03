import itertools

while True:
	n,x = map(int,input().split(" "))

	if n == 0 and x == 0:
		break

	#データリスト作成
	data = [m for m in range(1,n+1)]
	data_cmb = list(itertools.combinations(data,3))

	#検証
	res = [ret for ret in data_cmb if sum(ret) == x]
	print(len(res))

