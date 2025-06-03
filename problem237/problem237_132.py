n = int(input())
lr = [] # 各アームの左端と右端の位置のペア
for _ in range(n):
    x, l = list(map(int, input().split()))
    lr.append((x-l, x+l))

# 右端位置でソート
lr.sort(key=lambda x:x[1])

ans = 0
right = -10**9
for l,r in lr:
    # 重なってないなら残す
    if l >= right:
        ans += 1
        right = r

print(ans)