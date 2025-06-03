A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 割引券を使用しない場合は各品の最低金額合計が解となる
ans = min(a) + min(b)

# 割引券を使用して安くなるケースがないか調べる
for _ in range(M):
    x, y, c = map(int, input().split())
    tmp = a[x-1] + b[y-1] - c
    if tmp < ans:
        ans = tmp

print(ans)
