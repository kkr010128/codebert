N = int(input())
D = [list(map(int,input().split())) for _ in range(N)]

cnt = 0

for i in range(N):
    cnt = cnt + 1 if D[i][0] == D[i][1] else 0
    if cnt == 3:
        print('Yes')
        exit()

print('No')