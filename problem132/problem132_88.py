n, k = map(int, input().split())
alst = list(map(int, input().split()))

for _ in range(k):
    tmp = [0 for _ in range(n + 1)]
    for i, num in enumerate(alst):
        min_ind = max(i - num, 0)
        max_ind = min(i + num + 1, n)
        tmp[min_ind] += 1
        tmp[max_ind] -= 1
    next_num = 0
    for i, num in enumerate(tmp[:-1]):
        next_num += num
        alst[i] = next_num
    if tmp[0] == n and tmp[-1] == -n:
        break
print(*alst)