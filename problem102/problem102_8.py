N, K = [int(v) for v in input().strip().split(" ")]
A = [int(v) for v in input().strip().split(" ")]

for i in range(N - K):
    if A[i+K] > A[i]:
        print("Yes")
    else:
        print("No")