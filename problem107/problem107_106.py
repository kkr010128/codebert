n = int(input())
s = input()
pw, pw1, pw2 = [0] * n, [0] * n, [0] * n
pw[0], pw1[0], pw2[0] = 1, 1, 1
v, mod1, mod2 = 0, 0, 0
for i in range(n):
    if s[i] == '1':
        v += 1
for i in range(1, n):
    pw1[i] = int(pw1[i - 1] * 2) % (v + 1)
    if v >= 2:
        pw2[i] = int(pw2[i - 1] * 2) % (v - 1)
for i in range(n):
    if s[i] == '1':
        mod1 = (mod1 + pw1[n - i - 1]) % (v + 1)
        if v >= 2:
            mod2 = (mod2 + pw2[n - i - 1]) % (v - 1)    
for i in range(n):
    copy, x, cnt = 0, v, 1
    
    if s[i] == '0':
        x += 1
        copy = (mod1 + pw1[n - i - 1]) % x
    else:
        x -= 1
        if x >= 1:
            copy = (mod2 - pw2[n - i - 1]) % x
        else:
            copy = -1
    if copy == -1:
        print(0)
    else:
        x = bin(copy).count('1')
        while copy > 0:
            copy %= x
            x = bin(copy).count('1')
            cnt += 1
        print(cnt)
