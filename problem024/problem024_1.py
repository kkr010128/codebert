n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]

def check(p):
    i = 0
    for _ in range(k):
        s = 0
        while s + w[i] <= p:
            s += w[i]
            i += 1
            if i == n:
                return True
    return False

ng, ok = 0, 10**9
while ok-ng > 1:
    mid = (ng+ok)//2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)
