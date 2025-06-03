# F - Sugoroku
N, M = map(int, input().split())
S = str(input())

disable = False
answer = []
i = N
while i > 0:
    if i <= M:
        answer.append(i)
        break
        
    move = M
    while S[i - move] == "1":
        move -= 1

    if move == 0:
        disable = True
        break
        
    answer.append(move)
    i -= move
    
if disable:
    print(-1)
else:
    L = len(answer)
    for j in range(L):
        print(answer[L - j - 1], end=" ")