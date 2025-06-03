import random
import time
import copy
start = time.time()
D = int(input())
s = [[0 for j in range(26)] for i in range(D)]
c = list(map(int, input().split(" ")))
result = []
total = -10000000
for i in range(D):
    a = list(map(int, input().split(" ")))
    for j, k in enumerate(a):
        s[i][j] = int(k)
while(1):
    result_tmp = []
    total_tmp=0
    last = [0 for i in range(26)]
    for i in range(D):
        score = [0 for i in range(26)]

        for j in range(26):
            score[j] = s[i][j]
            for k in range(26):
                if j != k:
                    score[j] -= (i + 1 - last[k]) * c[k]
        score_sort = sorted(score, reverse=True)
        score_max = score_sort[0]

        tmp = []
        for j in range(26):
            if score_max >= 0 and score_max*0.95 <= score[j]:
                tmp.append(j)
            if score_max < 0 and score_max*1.05 <= score[j]:
                tmp.append(j)

        score_max = random.choice(tmp)

        result_tmp.append(score_max)
        last[score_max] = i + 1
        total_tmp += score[score_max]
    if total < total_tmp:
        total=total_tmp
        result = result_tmp.copy()
    end = time.time()
    if end - start > 1.8:
        break
for i in range(D):
    print(result[i]+1)
