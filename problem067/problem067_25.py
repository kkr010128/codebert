n = int(input())

score = [0, 0]
for i in range(n):
    c = input().split()
    if c[0] == c[1]:
        score[0] += 1
        score[1] += 1
    elif c[0] < c[1]:
        score[1] += 3
    else:
        score[0] += 3

print(*score)