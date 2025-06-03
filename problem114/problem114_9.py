import numpy as np
ans=0
D=int(input())
C=np.array(list(map(int,input().split())))
last_day=np.array([-1 for _ in range(26)])
score=np.array([list(map(int,input().split())) for _ in range(D)])

for day in range(D):
    t=int(input())-1
    last_day[t]=day
    tmp=C*(last_day-day)
    ans=ans+score[day][t]+sum(tmp)
    print(ans)


