import sys
input = sys.stdin.readline

n = int(input())
A = tuple(int(x) for x in input().split())
_ = int(input())
M = tuple(int(x) for x in input().split())

S = set()
def Check(i, s):
    if i == n:
        S.add(s)
        return
    Check(i + 1, s + A[i])
    Check(i + 1, s)

Check(0, 0)

for m in M:
    if m in S:
        print('yes')
    else:
        print('no')
