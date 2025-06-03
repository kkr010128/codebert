"""
一回以上わるとき、KはNの約数なので、Nの約数を全通り試して1に持っていけるかどうかを検証する。
Nを一回も割らずに1まで持っていけるようなKは、N-1の約数の数だけ存在する。
それぞれカウントすればよい
"""
N = int(input())
ans = 0
if N == 2:
    print(1)
    exit()

divisers = [N]
d = 2
while d*d < N:
    if N % d == 0:
        divisers.append(d)
        divisers.append(N//d)
    d += 1
if d**2 == N:
    divisers.append(d)

for d in divisers:
    dummyN = N
    while dummyN%d == 0:
        dummyN //= d
    if dummyN % d == 1:
        ans += 1

N -= 1
divisers = [N]
d = 2
while d*d < N:
    if N % d == 0:
        divisers.append(d)
        divisers.append(N//d)
    d += 1
if d**2 == N:
    divisers.append(d)

ans += len(divisers)

print(ans)