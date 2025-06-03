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
	N, R = getlist()
	if N >= 10:
		print(R)
	else:
		print(R + (10 - N) * 100)
	


if __name__ == '__main__':
	main()