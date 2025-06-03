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
cnt=0
score = [0 for i in range(26)]

while(1):
    cnt+=1
    result_tmp = []
    total_tmp = 0
    last = [0 for i in range(26)]
    for i in range(D):
        for j in range(26):
            score[j] = s[i][j]
            for k in range(26):
                if j != k:
                    score[j] -= (i + 1 - last[k]) * c[k]

        score_max = max(score)
        tmp = []
        
        for j in range(26):
            if score_max >= 0 and score_max*0.8 <= score[j]:
                tmp.append(j)
            if score_max < 0 and score_max*1.1 <= score[j]:
                tmp.append(j)

        score_max = random.choice(tmp)
        result_tmp.append(score_max)
        last[score_max] = i + 1
        total_tmp += score[score_max]
    if total < total_tmp:
        total = total_tmp
        result = result_tmp.copy()
    end = time.time()
    
    if end - start > 1.8:
        break
#print("total",total,cnt)
for i in range(D):
    print(result[i]+1)