N = int(input())
P = list(map(int, input().split()))

min_value = P[0]
cnt = 1
for i in range(1, N):
    if P[i] < min_value :
        min_value = P[i]
        cnt += 1

print(cnt)
