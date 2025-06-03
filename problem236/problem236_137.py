H = int(input())
W = int(input())
N = int(input())

ans = n = 0
while n < N:
    if H<W:
        n += W
        H -= 1
    else:
        n += H
        W -= 1
    ans += 1
print(ans)