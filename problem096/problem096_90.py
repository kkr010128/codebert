N,D = map(int, input().split())
XY_s = [list(map(int,input().split())) for _ in range(N)]
D**=2
answer = 0
for i in range(N):
    if D >= XY_s[i][0]**2 + XY_s[i][1]**2:
        answer+=1
print(answer)