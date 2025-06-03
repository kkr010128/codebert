H = int(input())
W = int(input())
N = int(input())

n = max(H, W)
ans = 1

while True:
    if n >= N:
        break

    n += max(H, W)
    ans += 1

print(ans)
