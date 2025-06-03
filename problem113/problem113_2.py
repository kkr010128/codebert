from time import time
start=time()
from copy import deepcopy
from random import randint

d=int(input())
c=list(map(int,input().split()))
s=[]
for i in range(d):
    a=list(map(int,input().split()))
    s.append(a)

def score_calculator(l):
    score=0
    las=[0]*26
    for i in range(d):
        for j in range(26):
            las[j]+=1
        las[l[i]]=0
        for j in range(26):
            score-=las[j]*c[j]
        score+=s[i][l[i]]
    return score
    
highest_sum_score=-1000000000000

for i in range(1,13):
    last=[0]*26
    temp_ans_lst=[]
    for j in range(d):
        daily_highest_score=-10000000000000
        for k in range(26):
            temp_score=s[j][k]
            temp_last=deepcopy(last)
            for p in range(26):
                temp_last[p]+=1
            temp_last[k]=0
            for p in range(26):
                down=temp_last[p]
                for q in range(i):
                    qdown=down+i+1
                    down+=qdown
                temp_score-=down*c[p]
            if temp_score>daily_highest_score:
                daily_highest_score=temp_score
                daily_choice=k
        for k in range(26):
            last[k]+=1
        last[daily_choice]=0
        temp_ans_lst.append(daily_choice)
    if score_calculator(temp_ans_lst)>highest_sum_score:
        ans_lst=deepcopy(temp_ans_lst)
        highest_sum_score=score_calculator(temp_ans_lst)
        
while time()-start<1.9:
    a=randint(0,d-1)
    b=randint(0,25)
    temp_ans_lst=deepcopy(ans_lst)
    temp_ans_lst[a]=b
    if score_calculator(temp_ans_lst)>highest_sum_score:
        ans_lst=deepcopy(temp_ans_lst)
        highest_sum_score=score_calculator(temp_ans_lst)

for i in ans_lst:
    print(i+1)