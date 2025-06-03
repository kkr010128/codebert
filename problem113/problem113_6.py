import time
import copy

start_time = time.time()

#input
D = int(input())
c_list = list(map(int, input().split()))

s_grid = []
for i in range(D):
    array = list(map(int, input().strip().split(' ')))
    s_grid.append(array)

def calculate_score(d,t,last):
    score = s_grid[d][t]
    last[t] = -1
    for i in range(26):
        score -= c_list[i]*(last[i]+1)
    return score

t_list = [] #task_list
last_list = [0] * 26

for k in range(0,D):
    X = -1  # k-日目に変える番号を探す
    p = 0
    for i in range(26):  # 26通り試す
        tmp = calculate_score(k,i,last_list)
        if tmp > p:
            X = i
            p = tmp

    #最大のXを投入
    t_list.append(X)
    last_list = [n+1 for n in last_list]
    last_list[X] = 0

    if time.time() - start_time > 1.9:
        break

for j in range(len(t_list)):
    print(int(t_list[j]) + 1)