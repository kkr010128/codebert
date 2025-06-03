import sys

n,k = map(int,sys.stdin.readline().split())
T = [int(sys.stdin.readline()) for _ in range(n)]

def check(P):
    i = 0
    for j in range(k):
        s = 0
        while (s + T[i] <= P):
            s += T[i]
            i += 1
            if i == n:
                return n
    return i

left = 0
right = 100000 * 10000

while (right - left > 1):
    mid = (left + right)//2
    v = check(mid)
    if v >= n:
        right = mid
    else:
        left = mid

print(right)
