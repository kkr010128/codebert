N, M = map(int, input().split())

cnt = 0

l = 0
k = M
while cnt < M and k > 0:
    print(l + 1, l + k + 1)
    cnt += 1
    l += 1
    k -= 2

l = M + 1
k = M - 1
while cnt < M:
    print(l + 1, l + k + 1)
    cnt += 1
    l += 1
    k -= 2
