N,D = map(int, input().split())

cnt = 0

for _ in range(N):
    X,Y = map(int, input().split())
    cnt += X*X + Y*Y <= D*D

print(cnt)