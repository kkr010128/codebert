from copy import deepcopy

d=int(input())
c=list(map(int,input().split()))
s=[]
for i in range(d):
    a=list(map(int,input().split()))
    s.append(a)

def score_calculator(l):
    score=0
    last=[0]*26
    for i in range(d):
        for j in range(26):
            last[j]+=1
        last[l[i]]=0
        for j in range(26):
            score-=last[j]*c[j]
        score+=s[i][l[i]]
    return score

for i in range(1,26):
    highest_sum_score=-1000000000000
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
        temp_ans_lst.append(daily_choice)
    if score_calculator(temp_ans_lst)>highest_sum_score:
        ans_lst=temp_ans_lst
        
for i in ans_lst:
    print(i+1)