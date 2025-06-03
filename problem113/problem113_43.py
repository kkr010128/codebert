import copy as cp
import time
import random

#INPUT
t_start = time.time()
D = int(input())
c = [int(i) for i in input().split()]
s = []
for i in range(D):
    new = [int(i) for i in input().split()]
    s.append(new)

#Utilitiy
def score(ans):
    if len(ans) != D:
        print("wrong length")
        return 0
    else:
        p = 0
        last = [-1]*26
        for i in range(D):
            contest = ans[i]-1
            p += s[i][contest]
            last[contest] = i
            for j in range(26):
                p -= c[j]*(i-last[j])
        return p

def greedy(ahead=0):
    ans = []
    p = 0
    last = [-1]*26
    for i in range(D):
        decay = 0
        for j in range(26):
            decay -= c[j]*(i-last[j])
            
        max_j = -1
        max_plus_mod = decay
        max_plus = decay
        for j in range(26):
            plus = s[i][j] + c[j]*(i-last[j])
            modify = c[j]*(ahead*(i-last[j])+ahead*(ahead+1)//2)
            if (plus+modify) > max_plus_mod:
                max_plus = plus
                max_plus_mod = plus+modify
                max_j = j
        ans.append(max_j+1)
        last[max_j]=i
        p += max_plus + decay
    return ans, p

def schedule(ans):
    dates = [[] for i in range(26)]
    for i in range(D):
        dates[ans[i]-1].append(i)
    return dates

def swap(ans):
    ans_temp = cp.copy(ans)
    t1 = random.randint(0,D-1)
    t2 = random.randint(0,D-1)
    temp = ans_temp[t1]
    ans_temp[t1] = ans_temp[t2]
    ans_temp[t2] = temp
    return ans_temp

def change(ans):
    ans_temp = cp.copy(ans)
    t = random.randint(0,D-1)
    A = random.randint(1,26)
    ans_temp[t] = A
    return ans_temp

        
#MAIN
max_points = -10000000
for k in range(20):
    ans_temp, points = greedy(ahead = k)
    #print(k, points, ans_temp)
    if points > max_points:
        max_points = points
        ans = cp.copy(ans_temp)
        
dates = schedule(ans)

count = 0
while True:
    if count % 100 == 0:
        t_now = time.time()
        if t_now-t_start > 1.8:
            break
    r = random.randint(0,1)
    if r == 0:
        ans_temp = swap(ans)
        points_temp = score(ans_temp)
    else:
        ans_temp = change(ans)
        points_temp = score(ans_temp)
    
    if points_temp > points:
        points = points_temp
        ans = cp.copy(ans_temp)


for i in range(D):
    print(ans[i])