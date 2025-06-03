n = int(input())
score = [0,0]
for _ in range(n):
    tc, hc = input().split()
    if tc == hc:
        score[0] += 1
        score[1] += 1
    elif tc > hc:
        score[0] += 3
    else:
        score[1] += 3
print(*score)
