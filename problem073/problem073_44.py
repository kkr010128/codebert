N = int(input())
cnt = 0
for a in range(1, N):
    for b in range(a, N, a):
        cnt += 1
print(cnt)

