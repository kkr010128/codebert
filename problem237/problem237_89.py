N = int(input())
X = [list(map(int, input().split())) for i in range(N)]
LR = [[x[0]-x[1], x[0] + x[1]] for x in X]
LR.sort(key=lambda x:x[1])

A = 1
right = LR[0][1]
for i in range(1, N):
    if right <= LR[i][0]:
        A += 1
        right = LR[i][1]
print(A)