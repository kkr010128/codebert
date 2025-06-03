N, A, B = map(int, input().split())

ans = 0

def odd():
    global ans
    ans += (B - A) // 2

if (B - A) % 2 == 0:
    odd()
else:
    if (N - B) <= (A - 1):
        ans += (N - B) + 1
        A += (N - B) + 1
        B = N
    else:
        ans += (A - 1) + 1
        B -= (A - 1) + 1
        A = 1
    odd()

print(ans)