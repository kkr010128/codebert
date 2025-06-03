N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

flag = 0
count = 0

for i in range(N):
    if D[i][0] == D[i][1]:
        count += 1
    else:
        count = 0
    if count >= 3:
        flag = 1
        break

if flag == 1:
    print('Yes')
else:
    print('No')