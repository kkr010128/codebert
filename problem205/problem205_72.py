n, p = map(int, input().split())

if p == 2:
    s = input()
    ans = 0
    for i in range(n):
        if int(s[i]) % 2 == 0:
            ans += i + 1
    print(ans)

elif p == 5:
    s = input()
    ans = 0
    for i in range(n):
        if int(s[i]) % 5 == 0:
            ans += i + 1
    print(ans)

else:
    s = input()[::-1]
    mod = 0
    c = [0] * p
    c[0] = 1
    ten = 1
    for i in s:
        mod = (mod + ten * int(i)) % p
        ten = ten * 10 % p
        c[mod] += 1

    ans = 0
    for i in c:
        ans += i * (i - 1) // 2
    print(ans)