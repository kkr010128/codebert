H ,W = map(int,input().split())

from collections import deque

S = [input() for i in range(H)]
directions = [[0,1],[1,0],[-1,0],[0,-1]]


counter = 0

#インデックス番号　xが行番号　yが列番号
for x in range(H):
    for y in range(W):
        if S[x][y]=="#":
            continue
         
        que =  deque([[x,y]])
        memory = [[-1]*W for _ in range(H)]
        memory[x][y]=0
       
        while True:
            if len(que)==0:
               break
            h,w = que.popleft()

            for i,k in directions:
                x_new,y_new = h+i,w+k

                if not(0<=x_new<=H-1) or not(0<=y_new<=W-1) :
                    continue
                
                elif not memory[x_new][y_new]==-1 or S[x_new][y_new]=="#":
                    continue

                memory[x_new][y_new] = memory[h][w]+1
                que.append([x_new,y_new]) 
        counter = max(counter,max(max(i) for i in memory))

print(counter)
