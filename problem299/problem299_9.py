def gotoS(org, n):
	res = [0] * n
	for i in range(1, n+1):
		res[org[i-1]-1] = i
	return res
n = int(input())
org = list(map(int, input().split()))
print(*gotoS(org, n))