n = list(map(int, input().split()))
w = [0] * n[0]
for i in range(n[0]):
    w[i] = int(input())
    
def check(p):
    i = 0
    for j in range(n[1]):
        s = 0
        while s + w[i] <= p:
            s += w[i]
            i += 1
            if i == n[0]:
                return True
    return False

def solve():
    left = 0
    right = 100000 * 10000
    min_p = 100000 * 10000
    while right - left > 1:
        mid = (right + left) // 2
        if check(mid):
            if min_p > mid:
                min_p = mid
            right = mid
        else:
            left = mid
    print(min_p)

solve()
