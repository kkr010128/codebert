n,x,y = map(int,input().split())
cnt_l = [0]*n
from collections import deque
# 幅優先探索
def bfs(start):
    queue = deque()
    queue.append(start)
    step_counts = [-1]*(n+1)
    step_counts[start] = 0
    while(queue):
        i = queue.popleft()
        cnt = step_counts[i]
        # 隣のグラフを取得
        if(i==x):
            nex_l = (i-1,y,i+1)
        elif(i==y):
            nex_l = (i-1,x,i+1)
        else:
            nex_l = (i-1,i+1)

        cnt += 1
        for j in nex_l:
            # 端より先だと止める
            if(j < 1 or n < j):
                continue
            # 訪問済みだと止める
            if(step_counts[j]!=-1):
                continue
            queue.append(j)
            step_counts[j] = cnt
            cnt_l[cnt] += 1

for i in range(1,n+1):
    bfs(i)

for i in range(1,n):
    # (a,b),(b,a)のペアがあるため//2
    print(cnt_l[i]//2)
