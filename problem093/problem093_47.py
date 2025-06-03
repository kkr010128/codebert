
# 公式解説を見てからやった
# 複数サイクルでき、1-K回移動可能
# N < 5000?多分、O(N * 2N)くらいで行けそうに見えるが。。。

def main(N,K,P,C):


	# 一度計算したサイクル情報を一応キャッシュしておく。。。
	# あんまり意味なさそう
	cycleIDs = [ -1 for _ in range(N) ]
	cycleInfs = []


	# print(P)

	ans = -1e10
	cycleID = 0

	for n in range(N):

		v = n
		currentCycleItemCnt = 0
		currentCycleTotal = 0

		if cycleIDs[v] != -1:
			currentCycleItemCnt, currentCycleTotal = cycleInfs[ cycleIDs[v] ]
			# print(currentCycleItemCnt, currentCycleTotal)
		else:
			while True:
				# 全頂点について、属するサイクルを計算する
				currentCycleItemCnt += 1
				currentCycleTotal += C[v]

				v = P[v]
				if v == n:
					# サイクル発見
					cycleInfs.append( (currentCycleItemCnt, currentCycleTotal) )
					cycleID += 1
					break

				# 一応、一度サイクルを計算した頂点については、
				# その頂点の属するサイクルの情報をメモっておく。。。
				cycleIDs[v] = cycleID

		procCnt = 0
		currentCycleSumTmp = 0

		while True:

			# 頂点vにコマが置かれた時の最高スコアを計算し、
			# これまでの最高スコアを上回ったら、これまでの最高スコアを更新する
			procCnt += 1
			currentCycleSumTmp += C[v]
			if K < procCnt:
				break

			cycleLoopCnt = 0
			if procCnt < K and 0 < currentCycleTotal:
				cycleLoopCnt = ( K - procCnt ) // currentCycleItemCnt

			# print("v=", v, "currentCycleSumTmp=", currentCycleSumTmp, procCnt)
			tmp = currentCycleSumTmp + cycleLoopCnt * currentCycleTotal
			ans = max( ans, tmp )

			v = P[v]
			if v == n:
				# サイクル終了
				break

	return ans
	# print(ans)



if __name__ == "__main__":
	N,K = map(int,input().split())
	P = [ int(p)-1 for p in input().split() ]
	C = list(map(int,input().split()))

	ans=main(N,K,P,C)
	print(ans)


