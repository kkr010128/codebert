def check(n, k, w, p):
    i = 0
    for j in range(k):
        s = 0
        while s + w[i] <= p:
            s += w[i]
            i += 1
            if i == n:
                return n
    return i
    
n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]

left, right = 0, 10 ** 10

while right - left > 1:
    mid = (left + right) // 2
    v = check(n, k, w, mid)
    if v >= n:
        right = mid
    else:
        left = mid

print(right)

