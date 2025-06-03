n = int(input())
bricks = list(map(int, input().split()))

cnt = 0
num = 1
for i in range(n):
    if bricks[i] == num: num += 1
    else: cnt += 1

else:
    if num != 1: print(cnt)
    else: print(-1)