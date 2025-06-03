
X = int(input())

n = X % 100
m = X // 100

cnt = 0
for a in reversed(range(1, 6)):
    while n - a >= 0:
        n -= a
        cnt += 1

if cnt <= m:
    print(1)
else:
    print(0)
