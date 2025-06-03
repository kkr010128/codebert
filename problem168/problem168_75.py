N, M = map(int, input().split())

A_list = list(map(int, input().split()))

for i in range(M):
    N -= A_list[i]
    if N < 0:
        print(-1)
        break
    if i == M-1:
        print(N)