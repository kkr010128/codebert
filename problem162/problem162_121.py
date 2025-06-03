N, M = map(int, input().split())

if N & 1:
    for m in range(1, M+1):
        print(m, N-m)

    exit()

n1, n2 = N//2, N//2
cnt = 0
for n in range(N//2):
    if n+1 >= N//2-n:
        break
    print(n+1, N//2-n)
    cnt += 1
    if cnt == M:
        exit()

for n in range(N//2):
    if n+1 >= N//2-n-1:
        break
    print(n+1+N//2, N-n-1)
    cnt += 1
    if cnt == M:
        exit()
