n = int(input())
a = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))

cnt = [0] * (2000 * 20)

for i in range(1, 2**n + 1):
    SUM = 0
    for j in range(n):
        if i>>j & 1:
            SUM += a[j]
    cnt[SUM] = 1

for _m in m:
    if cnt[_m] == 1:
        print("yes")
    else:
        print("no")
