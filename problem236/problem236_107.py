H = int(input())
W = int(input())
N = int(input())

cnt, paint = 0, 0
while paint < N:
    paint += max(H,W)
    cnt += 1
print(cnt)