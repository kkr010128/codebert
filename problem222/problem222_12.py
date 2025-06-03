number = int(input())
score = list(map(int,input().split()))
score.sort()
cancel = 0
for i in range(number-1):
    if score[i] == score[i+1]:
        cancel = 1
        break
if cancel == 1:
    print('NO')
else:
    print('YES')