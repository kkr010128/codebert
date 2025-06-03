N, D = map(int,input().split())
cnt = 0
for i in range(N):
    X,Y = map(int,input().split())
    S = (X**2+Y**2)**0.5
    if S <= D:
        cnt += 1
    else:
        continue
print(cnt)
