H = int(input())
W = int(input())
N = int(input())

ans = N // max(H, W)
if N % max(H, W) > 0:
    ans += 1

print(ans)