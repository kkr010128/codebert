N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
total = sum(A)
for a in A:
    if a >= total / (4*M):
        cnt += 1

ans = 'Yes' if cnt >= M else 'No'
print(ans)