N = int(input())
D = list(map(int,input().split()))
cnt = 0
for i in range(N):
    cnt += D[i]**2
tot = 0
for i in range(N):
    tot += D[i]
tot = tot**2
tot -= cnt
print(tot//2)