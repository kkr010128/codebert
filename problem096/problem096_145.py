N,D = map(int,input().split())
cnt = 0
for i in range(N):
    if sum(map(lambda x:x**2,map(int,input().split())))**0.5 <= D:
        cnt += 1
print(cnt)