n, k = (int(x) for x in input().split())

w = []
w = [int(input()) for i in range(n)]

def f(x):
    count = 0
    for i in range(k):
        s = 0
        while s + w[count] <= x:
            s += w[count]
            count += 1
            if count == n:
                return n
    return count

left = 0
right = 100000 * 100000

while right - left > 1:
    mid = (left + right) // 2
    v = f(mid)
    if v >= n:
        right = mid
    else:
        left = mid

print(right)
