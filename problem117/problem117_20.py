n,m,k = list(map(int,input().split(" ")))
a = list(map(int,input().split(" ")))
b = list(map(int,input().split(" ")))
cnt = 0
ans = 0
j = m
t = sum(b)

for i in range(n+1):
    while j>0:
        if t>k: #aのみの場合の処理が足りない（常にjでスキップされてしまう）
            j -= 1
            t -= b[j]
        else:break
    if t<=k:ans = max(ans,i+j)
    if i==n:break
    t += a[i]
print(ans)