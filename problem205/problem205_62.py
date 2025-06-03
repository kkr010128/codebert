import sys
input = sys.stdin.readline

n, p = map(int, input().split())

s = list(input().strip())

if p == 2 or p == 5:
    ans = 0
    while s:
        if p == 2 and int(s.pop()) % 2 == 0 or p == 5 and int(s.pop()) % 5 == 0:
            ans += n
        n -= 1
    print(ans)
    exit()

a = [0] * p

i = 1
k = 0
while s:
    k = (k + int(s.pop()) * i) % p
    a[k] += 1
    i *= 10
    i %= p

ans = a[0]
for i in a:
    if i >= 2:
        ans += i * (i - 1) // 2
print(ans)
