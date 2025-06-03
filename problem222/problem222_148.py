N = int(input())
A = [int(x) for x in input().split()]

cnt = dict()
for i in range(N):
    cnt[A[i]] = cnt.get(A[i], 0) + 1

if max(cnt.values()) > 1:
    print('NO')
else:
    print('YES')
