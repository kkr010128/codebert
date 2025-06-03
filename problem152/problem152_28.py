from collections import defaultdict
con = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N = int(input())	
	L = []
	Slist1 = []
	Slist2 = []
	R = []
	l = 0; r = 0
	for i in range(N):
		M = 0; end = None
		var = 0
		S = input()
		for j in S:
			if j == "(":
				var += 1
				l += 1
			else:
				var -= 1
				r += 1
			M = min(var, M)

		end = var
		if M == 0:
			L.append([M, end])
		elif M == end:
			R.append([M, end])
		elif M < 0 and end > 0:
			Slist1.append([-M, end])
		else:
			Slist2.append([M - end, M, end])
	
	Slist1 = sorted(Slist1)
	Slist2 = sorted(Slist2)
	if l != r:
		print("No")
		return

	cnt = 0
	X = len(L)
	for i in range(X):
		cnt += L[i][1]

	judge = "Yes"
	X = len(Slist1)
	for i in range(X):
		M = Slist1[i][0]
		cnt -= M
		if cnt < 0:
			judge = "No"
			break
		else:
			cnt += M + Slist1[i][1]

	X = len(Slist2)
	for i in range(X):
		cnt += Slist2[i][1]
		if cnt < 0:
			judge = "No"
			break
		else:
			cnt -= Slist2[i][0]

	print(judge)


if __name__ == '__main__':
	main()