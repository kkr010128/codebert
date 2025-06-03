n = int(input())
A = list(map(int,input().split()))
q = int(input())
M = list(map(int, input().split()))

d = {}

def solve(i, m):
    if m == 0:
        return True
    if i >= n:
        return False
    if (i, m) in d:
        return d[i, m]
    res = solve(i + 1,  m) or solve(i + 1, m - A[i])
    d[i,m] = res
    return res

for m in M:
    if solve(0, m):
        print('yes')
    else:
        print('no')

