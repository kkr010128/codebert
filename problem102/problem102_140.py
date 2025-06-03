N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for i in range(K, N):
    ans.append(['No', 'Yes'][A[i] > A[i - K]])

print('\n'.join(ans))