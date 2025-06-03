import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


s = S()
n = len(s)
ans = 0
cnt = 0
before_cnt = 0
now = s[0]
for x in s:
    if now == x:  # 同じ不等号が連続しているとき
        cnt += 1
    else:  # 不等号が変わるとき
        ans += cnt * (cnt + 1) // 2
        if now == '>':  # > から < に変わるとき
            if before_cnt < cnt:
                ans -= before_cnt
            else:
                ans -= cnt

        before_cnt = cnt
        cnt = 1
        now = x

ans += cnt * (cnt + 1) // 2
if now == '>':
    if before_cnt < cnt:
        ans -= before_cnt
    else:
        ans -= cnt
print(ans)
