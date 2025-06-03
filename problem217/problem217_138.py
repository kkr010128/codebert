if __name__ == '__main__':

	n = int(input())
	A = list(map(int,input().split()))

	cnt = 0
	for i in A:
		if i % 2 == 0:
			if i % 3 == 0 or i % 5 == 0:
				cnt += 1
		else:
			cnt += 1
	if cnt == n:
		print("APPROVED")
	else:
		print("DENIED")
