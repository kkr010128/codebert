N = int(input())
st = [list(input().split()) for _ in range(N)]
kyoku = input()
flg = False
ans = 0
for s, t in st:
    if flg:
        ans += int(t)
    if s == kyoku:
        flg = True
print(ans)