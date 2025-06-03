N, M = map(int,input().split())
accepted = [0]*N
wrong_ans =[0]*N 
for i in range(M):
    p,s = input().split()
    p = int(p)-1
    if s =="AC":
        accepted[p] = 1
    elif s == "WA" and accepted[p]==0:
        wrong_ans[p] = wrong_ans[p]+1

AC = 0
penalty = 0
for i in range(N):
    if accepted[i] == 1:
        AC = AC+1
        if wrong_ans[i]>=1:
            penalty = penalty+wrong_ans[i]
print(AC,penalty)