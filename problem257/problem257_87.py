n = int(input())
a = list(map(int,input().split()))

if 1 not in a:
    print(-1)
    exit()

x = 1
cnt = 0
for i in range(n):
    if a[i] == x:
        x += 1
    else:
        cnt += 1

print(cnt)