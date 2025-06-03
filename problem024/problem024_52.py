n, k = map(int, input().split())
w = [int(input()) for i in range(n)]
l = max(w)
r = sum(w)

while l < r:
    m = (l + r) // 2
    stack = car = 0
    for i in w:
        stack += i
        if stack > m:
            stack = i
            car += 1
    if car < k:
        r = m
    else:
        l = m + 1
print(l)