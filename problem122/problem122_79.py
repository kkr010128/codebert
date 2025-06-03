def main():
	N = int(input())
	A = [int(a) for a in input().split(" ")]
	S = sum(A)
	cA = [0] * 1000001
	for i in range(len(A)):
		cA[A[i]] += 1
	Q = int(input())
	for i in range(Q):
		B, C = [int(x) for x in input().split(" ")]
		diff = (C-B)*cA[B]
		S += diff
		cA[C] += cA[B]
		cA[B] = 0
		print(S)

main()
