K = int(input())
s = 7
flg = False
cnt = 0

for i in range(K+1):
    cnt += 1
    if s % K == 0:
        flg = True
        break
    s *= 10
    s %= K
    s += 7

if flg:
    print(cnt)
else:
    print(-1)
