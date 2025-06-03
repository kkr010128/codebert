N = int(input())
cnt = 0
for a in range(1, N):
    n = (N - 1) // a
    cnt += n

print(cnt)
