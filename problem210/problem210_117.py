def RSQ_add(i, x, y):
    while True:
        if i > n:
            break
        BIT[y][i] += x
        i += i & -i

def RSQ_getsum(i, x):
    s = 0
    while True:
        if i <= 0:
            break
        s += BIT[x][i]
        i -= i & -i
    return s

n = int(input())
s = list(input())
q = int(input())
BIT = [[0] * (n + 1) for _ in range(26)]
for i in range(n):
    y = ord(s[i]) - 97
    RSQ_add(i + 1, 1, y)
for _ in range(q):
    com, a, b = map(str, input().split())
    com, a = int(com), int(a)
    if com == 1:
        RSQ_add(a, -1, ord(s[a - 1]) - 97)
        RSQ_add(a, 1, ord(b) - 97)
        s[a - 1] = b
    else:
        b = int(b)
        ans = 0
        for i in range(26):
            if RSQ_getsum(b, i) - RSQ_getsum(a - 1, i) >= 1:
                ans += 1
        print(ans)