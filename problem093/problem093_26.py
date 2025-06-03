from itertools import accumulate

n, k = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

P = [p - 1 for p in P]

check = [False] * n
loops = []

for i in range(n):
    if check[i]:
        continue
    check[i] = True
    next = P[i]
    tmp = [i]
    while next != i:
        check[next] = True
        tmp.append(next)
        next = P[next]
    loops.append(tmp)

ans = int(-1e9)

for loop in loops:

    num = len(loop)
    div = k // num
    r = k % num
    if r == 0:
        r = num
        div -= 1
    L = [C[p] for p in loop]
    ans_tmp = int(-1e9)
    sumL = sum(L)
    by_loop = max(sumL, 0) * div
    if k > num and sumL <= 0:
        r = num
    L += L[:r]
    ACC = [0] + list(accumulate(L))

    for i in range(num):
        for j in range(i + 1, i + r + 1):
            ans_tmp = max(ans_tmp, ACC[j] - ACC[i] + by_loop)

    ans = max(ans, ans_tmp)
print(ans)
