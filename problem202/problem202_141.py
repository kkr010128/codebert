N, A, B = map(int, input().split())

# 周期
# 青 A個, 赤 B個

ans = N // (A + B) * A
n = N % (A + B)
if A <= n:
    ans += A
else:
    ans += n

print(ans)