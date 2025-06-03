MAX = 100000

def check(p):
    i = 0
    for j in range(k):
        s = 0
        while s + T[i] <= p:
            s = s + T[i]
            i = i + 1
            if i == n:
                return n
    return i

def solve():
    left = 0
    right = MAX * 10000
    while (right - left > 1):
        mid = (left + right) / 2
        v = check(mid)
        if v >= n:
            right = mid
        else:
            left = mid
    return right

n, k = map(int, raw_input().split())
T = []

for i in range(n):
    T.append(input())

ans = solve()

print ans