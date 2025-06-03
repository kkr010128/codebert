s = list(input())
k = int(input())
n = len(s)

ans = 0

# すべて同じ文字の場合
if s == [s[0]] * n:
    print((n*k)//2)
    exit(0)

# 先頭と末尾が異なる場合
i = 1
while i < n:
    if s[i-1] == s[i]:
        t = 2
        i+=1
        while i < n and s[i-1] == s[i]:
            t+=1
            i+=1
        ans += (t//2)*k
    i+=1
if s[0] != s[-1]:
    print(ans)
    exit(0)
# 先頭と末尾が一致する場合
# まず不一致の場合と同様に数えて、左右端の連続長さを数える
# 連結したとき、左右の1ブロックのみはそのまま数えられる
# 残りのk-1ブロックは、左右がつながった形で数えられる
i = 1
left = 1
right = 1
for i in range(n):
    if s[i] == s[i+1]:
        left += 1
    else:
        break
for i in range(n-1, -1, -1):
    if s[i] == s[i-1]:
        right += 1
    else:
        break
if s[0] == s[-1]:
    ans = ans - (k-1) * (left//2 + right//2) + (k-1) * ((left+right)//2)
    print(ans)
