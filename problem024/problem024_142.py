def check(k, W, p):
    s = 0
    count = 1
    for w in W:
        if s + w > p:
            count += 1
            s = 0
        s += w
    return count <= k

n, k = map(int, input().split())
W = [int(input()) for _ in range(n)]

right = sum(W)
left = max(right // k, max(W)) - 1
while right - left > 1:
    p = (left + right) // 2
    if check(k, W, p):
        right = p
    else:
        left = p
print(right)
