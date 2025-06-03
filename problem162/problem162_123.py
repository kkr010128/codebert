n, m = map(int, input().split())

a = (n - 1) // 2
d = 1
memo = set([])
cnt = 0
for i in range(m):

    if (n - d in memo) or (2*d == n):
        cnt += 1
        d += 1
    memo.add(d)
    if cnt > 1 or a < 1 or a+d > n:
        print(1/0)
    print(a, a+d)
    a -= 1
    d += 2
