N = int(input())
l = list(map(int,input().split()))

def is_ok(n, su):
    return l[n] > su

def binary_search(left, right, su):
    while (abs(right - left) > 1):
        mid = (left + right) // 2
        if is_ok(mid, su):  right = mid
        else:  left = mid
    return right

l = sorted(l)
ans = 0
for i in range(2, N):
    for j in range(1, i):
        left = j
        right = -1
        ret = binary_search(right, left, l[i] - l[j])
        if ret != right:  ans += j - ret
print(ans)