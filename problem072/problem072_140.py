N = int(input())
res = 0
cnt = 0
for i in range(N):
    D = input().split()
    if D[0] == D[1]:
        cnt += 1
        if cnt == 3:
            res += 1
            cnt = 0
    else:
        cnt = 0
if res > 0:
    print('Yes')
else:
    print('No')