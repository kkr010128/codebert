#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict

con = 10 ** 9 + 7
#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N = int(input())
	ansL = [[] for i in range(10)]
	ansL[0].append(["a", 1])
	for i in range(N - 1):
		n = len(ansL[i])
		for j in range(n):
			for k in range(ansL[i][j][1]):
				ansL[i + 1].append([ansL[i][j][0] + chr(97 + k), ansL[i][j][1]])
			ansL[i + 1].append([ansL[i][j][0] + chr(97 + ansL[i][j][1]), ansL[i][j][1] + 1])

	n = len(ansL[N - 1])
	for i in range(n):
		print(ansL[N - 1][i][0])
	



if __name__ == '__main__':
	main()