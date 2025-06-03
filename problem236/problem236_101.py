H = int(input())
W = int(input())
N = int(input())

cnt = 0
res = 0
while True:
    if cnt >= N:
        break
    cnt += max(H, W)
    res += 1

print(res)