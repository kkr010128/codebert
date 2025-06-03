import sys
def I(): return int(sys.stdin.readline().rstrip())
def S(): return sys.stdin.readline().rstrip()


N = I()
ST = [tuple(map(str,S().split())) for _ in range(N)]
X = S()

ans = 0
for i in range(N):
    s,t = ST[i]
    ans += int(t)
    if s == X:
        break

print(sum(int(ST[i][1]) for i in range(N))-ans)
