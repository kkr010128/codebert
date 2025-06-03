N = int(input())
A = list(map(int, input().split()))

pt = 1
cnt = 0
for i in range(N):
    if A[i] == pt:
        pt += 1
    else:
        cnt += 1

if cnt == N:
    print(-1)
else:
    print(cnt)