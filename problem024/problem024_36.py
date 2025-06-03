n, k = map(int, raw_input().split())
w = [int(raw_input()) for _ in xrange(n)]

def check(P):
    i = 0
    for j in range(k):
        s = 0
        while s + w[i] <= P:
            s += w[i]
            i += 1
            if i == n:
                return True
    return False


def solver():
    left, right = 0, 100000 * 10000

    while left < right:
        mid = int((left + right) / 2)

        if check(mid):
            right = mid
        else:
            left = mid + 1
    
    return right


print solver()