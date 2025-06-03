l, r, d = [int(x) for x in input().split(' ')]

cnt = 0
for i in range(0, 101, d):
    if l <= i and r >= i:
        cnt += 1

print(cnt)