import sys

N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

now = D[0]
zorome = 0
if now[0] == now[1]:
    zorome += 1
else:
    zorome = 0
for i in range(1, N):
    now = D[i]
    if now[0] == now[1]:
        zorome += 1
        if zorome == 3:
            print('Yes')
            sys.exit()
    else:
        zorome = 0
print('No')
