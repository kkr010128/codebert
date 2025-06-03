n = int(input())
lis = list(map(int, input().split()))

cnt = 0
a = 1
for i in range(n):
    if lis[i] == a:
        cnt += 1
        a += 1

if cnt == 0:
    print(-1)
else:
    print(n-cnt)