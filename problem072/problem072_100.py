N = int(input())
cnt = 0
flg = False
for _ in range(N):
    a, b = map(int, input().split())
    if a != b:
        cnt = 0
    else:
        cnt += 1
    if cnt >= 3:
        flg = True

if flg:
    print('Yes')
else:
    print('No')