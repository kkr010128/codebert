N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = ['Yes' if A[i] > A[i - K] else 'No' for i in range(K, N)]
print("\n".join(ans))