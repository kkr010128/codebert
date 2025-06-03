if __name__ == '__main__':

	n,m = map(int,input().split())

	A = [-1 for _ in range(n)]
	B = []
	for i in range(m):
		x,y = map(int,input().split())
		B.append([x,y])

	flg = True
	
	for a in B:
		x = a[0]
		y = a[1]

		if A[x-1] == -1:
			A[x-1] = y
		else:
			if A[x-1] != y:
				flg = False
				break

	ans = 0
	if flg:
		#穴埋め
		for i,j in enumerate(A):
			if j == -1:
				if i == 0 and len(A) != 1:
					A[i] = 1
				else:
					A[i] = 0

		tmp = ""
		for k in range(n):
			tmp += str(A[k])
		tmp = str(int(tmp))
		if len(tmp) == n :
			ans = int(tmp)
		else:
			ans = -1
	else:
		ans = -1

	print(ans)
