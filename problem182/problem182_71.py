#ライブラリインポート
from collections import defaultdict

con = 10 ** 9 + 7
#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N, K, C = getlist()
	S = list(input())
	D1 = defaultdict(int)
	D2 = defaultdict(int)
	var = - float("inf")
	cnt = 0
	for i in range(N):
		if S[i] == "o":
			if i - var >= C + 1:
				cnt += 1
				var = i
				D1[i] += 1

	if cnt >= K + 1:
		return

	#詰める
	var = float("inf")
	cnt = 0
	for i in range(N):
		if S[N - 1 - i] == "o":
			if var - (N - 1 - i) >= C + 1:
				cnt += 1
				var = N - 1 - i
				D2[N - 1 - i] += 1

	# print(D1)
	# print(D2)

	ans = []
	for i in D1:
		if D2[i] == 1:
			ans.append(i)

	ans = sorted(ans)
	for i in ans:
		print(i + 1)

if __name__ == '__main__':
	main()