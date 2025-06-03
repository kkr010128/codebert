def main():
	N = int(input())
	A = [int(a) for a in input().split(" ")]
	target = 1
	broke = 0
	for i in range(len(A)):
		if A[i] == target:
			target += 1
		else:
			broke += 1
	if broke < N:
		print(broke)
	else:
		print(-1)

main()