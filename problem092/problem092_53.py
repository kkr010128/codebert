#ABC 175 C
x, k, d = map(int, input().split())

x = abs(x)
syou = x // d
amari = x % d

if k <= syou:
    ans = x - (d * k)

else:
    if (k - syou) % 2 == 0: #残りの動ける数が偶数
        ans = amari

    else:#残りの動ける数が奇数
        ans = abs(amari - d)

print(ans)