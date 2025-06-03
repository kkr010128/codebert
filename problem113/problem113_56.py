import random
D = int(input())
last = [0 for i in range(26)]
s = [[0 for j in range(26)] for i in range(D)]
c = list(map(int, input().split(" ")))
result = []
for i in range(D):
    a = list(map(int, input().split(" ")))
    score = [0 for i in range(26)]
    for j, k in enumerate(a):
        s[i][j] = int(k)
    for j in range(26):
        score[j] = s[i][j]
        for k in range(26):
            if j != k:
                score[j] -= (i + 1 - last[k]) * c[k]
    score_sort = sorted(score,reverse=True)
    score_max = random.choice(score_sort[:1])
    for j in range(26):
        if score_max == score[j]:
            result.append(j)
            last[j] = i

for i in range(D):
    print(result[i]+1)


