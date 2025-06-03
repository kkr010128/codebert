# coding: utf-8
# Your code here!


def check(P):
    i = 0
    for j in range(k):
        s = 0
        while s + T[i] <= P:
            s += T[i]
            i += 1
            if i == n:
                return n
    return i
    
def solve():
    left = 0
    right = 100000 * 10000
    mid = 0
    while right - left > 1:
        mid = (left + right) // 2
        v = check(mid)
        if v >= n:
            right = mid
        else:
            left = mid
    return right
    
tmp = list(map(int, input().split())) 
n = tmp[0]
k = tmp[1]
T = []
for i in range(n):
    T.append(int(input()))
ans = solve()
print(ans)
    




