n = int(input())

a = list(map(int, input().split()))

cnt = 0
ave = sum(a)/2

for i in range(n):
    cnt += a[i]
    if cnt >= ave:
        ans = min(cnt*2-ave*2, ave*2-(cnt-a[i])*2)
        break

print(int(ans))