x, y = map(int, input().split())

answer = 0

for a in [x, y]:
    if a == 3:
        answer += 100000
    elif a == 2:
        answer += 200000
    elif a == 1:
        answer += 300000
    else:
        pass
if x == 1 and y == 1:
    answer += 400000

print(answer)
