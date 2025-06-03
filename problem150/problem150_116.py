#D
from collections import deque
n,k = map(int,input().split())
a = list(map(int,input().split()))
tel = deque()
tel.append(1)
visit = [False for _ in range(n)]
visit[0] = True
for i in range(n):
    nx = a[tel[i]-1]
    if visit[nx-1] == True :
        tel.append(nx)
        #ループの始まりのindexをidxに格納
        idx = tel.index(nx)
        break
    tel.append(nx)
    visit[nx-1] = True
    
#print(tel)
#print(visit)
if k <= idx:
    goal = tel[k]
else:
    k -= idx
    loop_num = len(tel) - idx - 1
    #print('idx:',idx)
    #print('loop_num:',loop_num)
    goal = tel[idx + k%loop_num]
    
print(goal)