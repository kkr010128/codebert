N = int(input())
ls = list(map(int,input().split()))
cnt = [0] * (N+1)

for i in range(N-1):
    cnt[ls[i]] += 1
    
for i in range(1,N+1):
    print(cnt[i])