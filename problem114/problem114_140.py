# coding: utf-8

D = int(input())
C = list(map(int,input().split()))
S = []
for i in range(D):
    s = list(map(int,input().split()))
    S.append(s)
    
#S = [0] + S
day_of_problems = [0] * 27
past = []
#def cal_last(i):#満足度低下の計算
 #   if i in past:
  #      return past.index(i)
ans = 0
for i in range(D):#i+1日目
    t = int(input())
    day_of_problems[t] = i+1
    ans += S[i][t-1]
    for j in range(26):
        ans -= C[j] * (i+1-day_of_problems[j+1])
    print(ans)