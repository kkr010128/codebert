X, Y = map(int, input().split())
prize = [300000, 200000, 100000]
ans = 0

if X <= 3:
    X -= 1
    ans += prize[X]

if Y <= 3:
    Y -= 1
    ans += prize[Y]

if ans == 600000:
    ans += 400000

print(ans)