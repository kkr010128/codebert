import sys; input = sys.stdin.buffer.readline
from collections import defaultdict
con = 998244353; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N, S = getlist()
	A = getlist()
	DP = [[0] * (S + 1) for i in range(N + 1)]
	DP[0][0] = 1
	for i in range(N):
		for j in range(S + 1):
			DP[i + 1][j] += 2 * DP[i][j]
			DP[i + 1][j] %= con
			w = A[i]
			if j + w <= S:
				DP[i + 1][j + w] += DP[i][j]
				DP[i + 1][j + w] %= con

	print(DP[-1][-1])


if __name__ == '__main__':
	main()