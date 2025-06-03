import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n = int(input())

def bs(ok, ng, solve):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok

ans = bs(n, 0, lambda x: x * 1.08 >= n)
if int(ans * 1.08) == n:
    print(ans)
else:
    print(':(')
