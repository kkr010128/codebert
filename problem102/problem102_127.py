import sys

N, K = map(int, input().split())
A = [0] + list(map(int, sys.stdin.readline().rsplit()))

for i in range(K + 1, N + 1):
    if A[i - K] < A[i]:
        print("Yes")
    else:
        print("No")
