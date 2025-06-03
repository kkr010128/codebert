# pythonの場合、ライブラリ関数でgcdがある？ただし、配列まとめてというわけではない模様
from math import gcd

def main():
	N = int(input())
	A = list(map(int,input().split()))

	pc = True
	maxA = max(A)

	cnts = [ 0 for _ in range(maxA+1) ]
	for a in A:
		cnts[a] += 1
	for i in range(2,maxA):
		if pc:
			# 素因数ごとに、A内での登場回数を数える
			# 2つあったらその2つのcommon dividerとして、1以外にそれがあることが確定する
			cnt = 0
			for j in range(i,maxA+1,i):
				cnt += cnts[j]
				if 1 < cnt:
					# Aの素因数で重複があれば、pcでない
					pc = False
					break

	sc = False

	if pc == False:
		gcdResult = 0
		for a in A:
			# 配列全要素に対してgcdを呼んでるが、結果的に、それが1になればsc、ならなければnot sc
			gcdResult=gcd(gcdResult,a)
		if gcdResult == 1:
			sc = True

	if pc:
		print("pairwise coprime")
	elif sc:
		print("setwise coprime")
	else:
		print("not coprime")






if __name__ == "__main__":
	main()

