N = int(input())
P = list(map(int, input().split()))

c_min = P[0]
cnt = 1

for i in range(1,N):
    if c_min >= P[i]:
        cnt += 1
    c_min = min(c_min,P[i])

print(cnt)