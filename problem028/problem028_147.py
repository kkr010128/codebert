
if __name__ == '__main__':
	n = input().split()
	c = input().split()
	dp = [50000] * (int(n[0]) + 1)

	for i in range(int(n[1])):
		if int(c[i]) > int(n[0]):
			continue
		dp[int(c[i])] = 1
		for j in range(int(n[0])):
			if int(c[i])+j > int(n[0]):
				break;
			if dp[j] != 50000:
				dp[int(c[i])+j] = min(dp[int(c[i])+j], dp[j]+1)

	print (dp[int(n[0])])


