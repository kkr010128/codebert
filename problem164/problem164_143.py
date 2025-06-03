a, b, c, d = map(int, input().split())

cnt1 = 0
cnt2 = 0
while c > 0:
    c -= b
    cnt1 += 1

while a > 0:
    a -= d
    cnt2 += 1

if cnt1 <= cnt2:
    print('Yes')
else:
    print('No')